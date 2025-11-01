"""Spoonacular API provider - Supports budget, used/missing ingredients"""
import requests
import time
from typing import List, Optional
from core.model import Recipe, Provider, IngredientItem
from core.normalize import normalize_ingredient_name

# Spoonacular API base URL
BASE_URL = "https://api.spoonacular.com"

# Rate limiting
RATE_LIMIT_DELAY = 0.1  # seconds between requests


class SpoonacularProvider:
    """Provider for Spoonacular API"""
    
    def __init__(self, api_key: str):
        """
        Initialize provider with API key.
        
        Args:
            api_key: Spoonacular API key
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RecipeFinder/1.0'
        })
        self.last_request_time = 0
    
    def _rate_limit(self):
        """Ensure we don't exceed rate limits"""
        elapsed = time.time() - self.last_request_time
        if elapsed < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - elapsed)
        self.last_request_time = time.time()
    
    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Make API request with rate limiting and error handling.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
        
        Returns:
            JSON response as dict
        
        Raises:
            Exception: If request fails
        """
        self._rate_limit()
        
        url = f"{BASE_URL}/{endpoint}"
        
        # Add API key to params
        if params is None:
            params = {}
        params['apiKey'] = self.api_key
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Spoonacular API request failed: {e}")
    
    def search_by_ingredients(
        self,
        ingredients: List[str],
        max_results: int = 10,
        ranking: int = 1  # 1 = maximize used ingredients, 2 = minimize missing
    ) -> List[dict]:
        """
        Search recipes by ingredients ("what's in your fridge" style).
        
        Args:
            ingredients: List of ingredient names
            max_results: Maximum number of results
            ranking: Ranking strategy
        
        Returns:
            List of recipe data from API
        """
        params = {
            'ingredients': ','.join(ingredients),
            'number': max_results,
            'ranking': ranking,
            'ignorePantry': True  # Don't assume user has pantry staples
        }
        
        return self._make_request("recipes/findByIngredients", params)
    
    def get_recipe_information(
        self,
        recipe_id: int,
        include_nutrition: bool = False
    ) -> dict:
        """
        Get detailed recipe information by ID.
        
        Args:
            recipe_id: Spoonacular recipe ID
            include_nutrition: Include nutrition data
        
        Returns:
            Recipe data
        """
        params = {
            'includeNutrition': str(include_nutrition).lower()
        }
        
        return self._make_request(f"recipes/{recipe_id}/information", params)
    
    def get_price_breakdown(self, recipe_id: int) -> Optional[dict]:
        """
        Get price breakdown for a recipe.
        
        Args:
            recipe_id: Spoonacular recipe ID
        
        Returns:
            Price breakdown data or None if not available
        """
        try:
            return self._make_request(f"recipes/{recipe_id}/priceBreakdownWidget.json")
        except Exception:
            return None
    
    def recipe_to_model(
        self,
        recipe_data: dict,
        detailed_info: dict,
        user_ingredients: List[str]
    ) -> Recipe:
        """
        Convert Spoonacular recipe data to our Recipe model.
        
        Args:
            recipe_data: Data from findByIngredients endpoint
            detailed_info: Data from recipe information endpoint
            user_ingredients: User's available ingredients
        
        Returns:
            Recipe object
        """
        # Extract used and missing ingredients
        used_ingredients = [
            ing['name'] for ing in recipe_data.get('usedIngredients', [])
        ]
        missing_ingredients = [
            ing['name'] for ing in recipe_data.get('missedIngredients', [])
        ]
        
        # Build ingredient items from detailed info
        ingredient_items = []
        for ing in detailed_info.get('extendedIngredients', []):
            ingredient_items.append(IngredientItem(
                name=ing.get('name', ''),
                quantity=str(ing.get('amount', '')) if ing.get('amount') else None,
                unit=ing.get('unit', '')
            ))
        
        # Extract diet/category info
        categories = []
        if detailed_info.get('cuisines'):
            categories.extend(detailed_info['cuisines'])
        if detailed_info.get('dishTypes'):
            categories.extend(detailed_info['dishTypes'])
        if detailed_info.get('diets'):
            categories.extend(detailed_info['diets'])
        
        # Get instructions
        instructions = detailed_info.get('instructions', '')
        if not instructions and detailed_info.get('analyzedInstructions'):
            # Build instructions from steps
            steps = []
            for instruction_set in detailed_info['analyzedInstructions']:
                for step in instruction_set.get('steps', []):
                    steps.append(f"{step['number']}. {step['step']}")
            instructions = '\n'.join(steps)
        
        return Recipe(
            id=str(recipe_data['id']),
            provider=Provider.SPOONACULAR,
            title=recipe_data.get('title', 'Unknown'),
            image_url=recipe_data.get('image'),
            source_url=detailed_info.get('sourceUrl') or detailed_info.get('spoonacularSourceUrl'),
            ingredients=ingredient_items,
            used_ingredients=used_ingredients,
            missing_ingredients=missing_ingredients,
            instructions=instructions,
            servings=detailed_info.get('servings'),
            ready_in_minutes=detailed_info.get('readyInMinutes'),
            cuisine=detailed_info.get('cuisines', [None])[0] if detailed_info.get('cuisines') else None,
            category_or_diet=categories,
            cost_per_serving_usd=None  # Will be filled separately
        )
    
    def search_with_filters(
        self,
        ingredients: List[str],
        max_results: int = 10,
        diet: Optional[str] = None,
        max_minutes: Optional[int] = None,
        max_cost: Optional[float] = None,
        exclude: Optional[List[str]] = None
    ) -> List[Recipe]:
        """
        Search recipes with filters.
        
        Args:
            ingredients: List of ingredient names
            max_results: Maximum number of results
            diet: Dietary preference
            max_minutes: Maximum cooking time
            max_cost: Maximum cost per serving (USD)
            exclude: Ingredients to exclude
        
        Returns:
            List of Recipe objects
        """
        print(f"🔍 Searching Spoonacular for recipes with: {', '.join(ingredients)}")
        
        # First, search by ingredients
        recipe_results = self.search_by_ingredients(ingredients, max_results * 2)
        
        if not recipe_results:
            print("  ✗ No recipes found")
            return []
        
        print(f"  ✓ Found {len(recipe_results)} candidate recipes")
        
        recipes = []
        
        for recipe_data in recipe_results:
            try:
                # Get detailed information
                detailed_info = self.get_recipe_information(recipe_data['id'])
                
                # Apply diet filter
                if diet:
                    recipe_diets = [d.lower() for d in detailed_info.get('diets', [])]
                    if diet.lower() not in recipe_diets:
                        continue
                
                # Apply time filter
                if max_minutes and detailed_info.get('readyInMinutes'):
                    if detailed_info['readyInMinutes'] > max_minutes:
                        continue
                
                # Apply exclude filter
                if exclude:
                    recipe_ings = [
                        ing.get('name', '').lower()
                        for ing in detailed_info.get('extendedIngredients', [])
                    ]
                    if any(excl.lower() in recipe_ings for excl in exclude):
                        continue
                
                # Convert to our model
                recipe = self.recipe_to_model(recipe_data, detailed_info, ingredients)
                
                # Get price information if cost filter is specified
                if max_cost is not None:
                    price_data = self.get_price_breakdown(recipe_data['id'])
                    if price_data and 'totalCostPerServing' in price_data:
                        # Spoonacular returns cost in cents
                        cost_per_serving = price_data['totalCostPerServing'] / 100.0
                        recipe.cost_per_serving_usd = cost_per_serving
                        
                        # Apply cost filter
                        if cost_per_serving > max_cost:
                            continue
                
                recipes.append(recipe)
                
                if len(recipes) >= max_results:
                    break
                    
            except Exception as e:
                print(f"  ⚠️  Error processing recipe {recipe_data.get('id')}: {e}")
                continue
        
        print(f"  ✓ Returning {len(recipes)} recipes after filtering")
        
        return recipes


def search_recipes(
    ingredients: List[str],
    max_results: int = 10,
    diet: Optional[str] = None,
    max_minutes: Optional[int] = None,
    max_cost: Optional[float] = None,
    exclude: Optional[List[str]] = None,
    api_key: str = None,
    **kwargs
) -> List[Recipe]:
    """
    Main entry point for Spoonacular recipe search.
    
    Args:
        ingredients: List of ingredient names
        max_results: Maximum number of results
        diet: Dietary preference
        max_minutes: Maximum cooking time
        max_cost: Maximum cost per serving
        exclude: Ingredients to exclude
        api_key: Spoonacular API key
        **kwargs: Additional parameters (ignored)
    
    Returns:
        List of Recipe objects
    """
    if not api_key:
        raise ValueError("Spoonacular API key is required")
    
    provider = SpoonacularProvider(api_key)
    return provider.search_with_filters(
        ingredients=ingredients,
        max_results=max_results,
        diet=diet,
        max_minutes=max_minutes,
        max_cost=max_cost,
        exclude=exclude
    )

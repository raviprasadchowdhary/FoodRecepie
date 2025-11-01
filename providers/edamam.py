"""Edamam Recipe Search API provider - Strong diet and nutrition filters"""
import requests
import time
from typing import List, Optional
from core.model import Recipe, Provider, IngredientItem
from core.normalize import find_matching_ingredients

# Edamam API base URL
BASE_URL = "https://api.edamam.com/api/recipes/v2"

# Rate limiting
RATE_LIMIT_DELAY = 0.2  # seconds between requests


class EdamamProvider:
    """Provider for Edamam Recipe Search API v2"""
    
    def __init__(self, app_id: str, app_key: str):
        """
        Initialize provider with API credentials.
        
        Args:
            app_id: Edamam application ID
            app_key: Edamam application key
        """
        self.app_id = app_id
        self.app_key = app_key
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
    
    def _make_request(self, params: dict) -> dict:
        """
        Make API request with rate limiting and error handling.
        
        Args:
            params: Query parameters
        
        Returns:
            JSON response as dict
        
        Raises:
            Exception: If request fails
        """
        self._rate_limit()
        
        # Add API credentials to params
        params['app_id'] = self.app_id
        params['app_key'] = self.app_key
        params['type'] = 'public'  # Recipe type
        
        try:
            response = self.session.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Edamam API request failed: {e}")
    
    def recipe_to_model(
        self,
        recipe_data: dict,
        user_ingredients: List[str]
    ) -> Recipe:
        """
        Convert Edamam recipe data to our Recipe model.
        
        Args:
            recipe_data: Recipe data from API
            user_ingredients: User's available ingredients
        
        Returns:
            Recipe object
        """
        recipe = recipe_data.get('recipe', {})
        
        # Extract ingredient names
        recipe_ingredient_names = [
            ing.get('food', '') for ing in recipe.get('ingredients', [])
        ]
        
        # Build ingredient items
        ingredient_items = []
        for ing in recipe.get('ingredients', []):
            ingredient_items.append(IngredientItem(
                name=ing.get('food', ''),
                quantity=str(ing.get('quantity', '')) if ing.get('quantity') else None,
                unit=ing.get('measure', '')
            ))
        
        # Determine used vs missing
        used, missing = find_matching_ingredients(user_ingredients, recipe_ingredient_names)
        
        # Extract categories/diet/health labels
        categories = []
        if recipe.get('cuisineType'):
            categories.extend(recipe['cuisineType'])
        if recipe.get('mealType'):
            categories.extend(recipe['mealType'])
        if recipe.get('dishType'):
            categories.extend(recipe['dishType'])
        if recipe.get('dietLabels'):
            categories.extend(recipe['dietLabels'])
        
        # Extract time (Edamam provides total time)
        total_time = recipe.get('totalTime', 0)
        ready_in_minutes = int(total_time) if total_time else None
        
        # Get cuisine (first one if multiple)
        cuisine = recipe.get('cuisineType', [None])[0] if recipe.get('cuisineType') else None
        
        return Recipe(
            id=recipe.get('uri', '').split('#')[-1],  # Extract ID from URI
            provider=Provider.EDAMAM,
            title=recipe.get('label', 'Unknown'),
            image_url=recipe.get('image'),
            source_url=recipe.get('url'),
            ingredients=ingredient_items,
            used_ingredients=used,
            missing_ingredients=missing,
            instructions=None,  # Edamam doesn't provide instructions
            servings=int(recipe.get('yield', 0)) if recipe.get('yield') else None,
            ready_in_minutes=ready_in_minutes,
            cuisine=cuisine,
            category_or_diet=categories,
            cost_per_serving_usd=None  # Edamam doesn't provide cost
        )
    
    def search_recipes(
        self,
        ingredients: List[str],
        max_results: int = 10,
        diet: Optional[str] = None,
        health: Optional[List[str]] = None,
        max_minutes: Optional[int] = None,
        exclude: Optional[List[str]] = None
    ) -> List[Recipe]:
        """
        Search recipes with filters.
        
        Args:
            ingredients: List of ingredient names
            max_results: Maximum number of results
            diet: Dietary preference (balanced, high-protein, low-carb, low-fat)
            health: Health restrictions (vegan, vegetarian, dairy-free, etc.)
            max_minutes: Maximum cooking time
            exclude: Ingredients to exclude
        
        Returns:
            List of Recipe objects
        """
        print(f"🔍 Searching Edamam for recipes with: {', '.join(ingredients)}")
        
        # Build query from ingredients
        query = ' '.join(ingredients)
        
        params = {
            'q': query,
            'to': max_results
        }
        
        # Add diet filter
        if diet:
            # Map our diet values to Edamam diet values
            diet_map = {
                'vegetarian': 'balanced',  # Edamam doesn't have vegetarian diet
                'vegan': 'balanced',
                'gluten-free': 'balanced',
                'ketogenic': 'low-carb',
                'paleo': 'balanced'
            }
            edamam_diet = diet_map.get(diet.lower(), 'balanced')
            params['diet'] = edamam_diet
        
        # Add health filters
        if health:
            # Map our health values to Edamam health labels
            health_map = {
                'nut-free': 'tree-nut-free',
                'dairy-free': 'dairy-free',
                'egg-free': 'egg-free',
                'soy-free': 'soy-free',
                'fish-free': 'fish-free'
            }
            
            for h in health:
                edamam_health = health_map.get(h.lower(), h.lower())
                if 'health' not in params:
                    params['health'] = []
                if isinstance(params['health'], list):
                    params['health'].append(edamam_health)
        
        # Handle special diet mappings for health
        if diet:
            if diet.lower() == 'vegetarian':
                if 'health' not in params:
                    params['health'] = []
                if isinstance(params['health'], list):
                    params['health'].append('vegetarian')
            elif diet.lower() == 'vegan':
                if 'health' not in params:
                    params['health'] = []
                if isinstance(params['health'], list):
                    params['health'].append('vegan')
        
        # Add time filter (Edamam uses time in minutes)
        if max_minutes:
            params['time'] = f'1-{max_minutes}'
        
        # Add excluded ingredients
        if exclude:
            params['excluded'] = exclude
        
        try:
            data = self._make_request(params)
            
            hits = data.get('hits', [])
            if not hits:
                print("  ✗ No recipes found")
                return []
            
            print(f"  ✓ Found {len(hits)} recipes")
            
            recipes = []
            for hit in hits[:max_results]:
                try:
                    recipe = self.recipe_to_model(hit, ingredients)
                    recipes.append(recipe)
                except Exception as e:
                    print(f"  ⚠️  Error processing recipe: {e}")
                    continue
            
            print(f"  ✓ Returning {len(recipes)} recipes")
            
            return recipes
            
        except Exception as e:
            print(f"  ✗ Search failed: {e}")
            return []


def search_recipes(
    ingredients: List[str],
    max_results: int = 10,
    diet: Optional[str] = None,
    health: Optional[List[str]] = None,
    max_minutes: Optional[int] = None,
    exclude: Optional[List[str]] = None,
    app_id: str = None,
    app_key: str = None,
    **kwargs
) -> List[Recipe]:
    """
    Main entry point for Edamam recipe search.
    
    Args:
        ingredients: List of ingredient names
        max_results: Maximum number of results
        diet: Dietary preference
        health: Health restrictions
        max_minutes: Maximum cooking time
        exclude: Ingredients to exclude
        app_id: Edamam application ID
        app_key: Edamam application key
        **kwargs: Additional parameters (ignored)
    
    Returns:
        List of Recipe objects
    """
    if not app_id or not app_key:
        raise ValueError("Edamam API credentials are required")
    
    provider = EdamamProvider(app_id, app_key)
    return provider.search_recipes(
        ingredients=ingredients,
        max_results=max_results,
        diet=diet,
        health=health,
        max_minutes=max_minutes,
        exclude=exclude
    )

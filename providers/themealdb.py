"""TheMealDB API provider - Free tier with no authentication required"""
import time
from typing import List, Optional, Set
from core.model import Recipe, Provider, IngredientItem
from core.normalize import (
    normalize_for_themealdb,
    normalize_ingredient_name,
    ingredients_match,
    find_matching_ingredients
)
from core.performance import cached, get_http_session

# TheMealDB API base URL
BASE_URL = "https://www.themealdb.com/api/json/v1/1"

# Test/development key (free tier)
API_KEY = "1"

# Rate limiting
RATE_LIMIT_DELAY = 0.1  # seconds between requests (reduced from 0.5)
REQUEST_TIMEOUT = 3  # seconds (reduced from 10)


class TheMealDBProvider:
    """Provider for TheMealDB API"""
    
    def __init__(self):
        # Use shared session pool for better performance
        self.session = get_http_session("themealdb")
        self.last_request_time = 0
        self.api_available = True  # Track if API is available
    
    def _rate_limit(self):
        """Ensure we don't exceed rate limits (only if API is working)"""
        if not self.api_available:
            return  # Skip delay if API is down
        
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
        
        try:
            response = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            self.api_available = True  # Mark as available on success
            return response.json()
        except Exception as e:
            self.api_available = False  # Mark as unavailable on failure
            raise Exception(f"TheMealDB API request failed: {e}")
    
    @cached(ttl=3600)  # Cache for 1 hour
    def filter_by_ingredient(self, ingredient: str) -> Set[str]:
        """
        Get meal IDs that contain the specified ingredient.
        
        Args:
            ingredient: Ingredient name
        
        Returns:
            Set of meal IDs
        """
        # Normalize ingredient for API
        normalized = normalize_for_themealdb(ingredient)
        
        try:
            data = self._make_request("filter.php", {"i": normalized})
            
            if not data.get("meals"):
                return set()
            
            return {meal["idMeal"] for meal in data["meals"]}
        except Exception as e:
            print(f"Warning: Failed to filter by ingredient '{ingredient}': {e}")
            return set()
    
    @cached(ttl=7200)  # Cache for 2 hours (recipes don't change often)
    def lookup_meal(self, meal_id: str) -> Optional[dict]:
        """
        Get full meal details by ID.
        
        Args:
            meal_id: TheMealDB meal ID
        
        Returns:
            Meal data or None if not found
        """
        try:
            data = self._make_request("lookup.php", {"i": meal_id})
            
            if not data.get("meals"):
                return None
            
            return data["meals"][0]
        except Exception as e:
            print(f"Warning: Failed to lookup meal {meal_id}: {e}")
            return None
    
    def extract_ingredients_from_meal(self, meal: dict) -> List[str]:
        """
        Extract ingredient names from meal data.
        
        TheMealDB stores ingredients in fields strIngredient1..20
        
        Args:
            meal: Meal data from API
        
        Returns:
            List of ingredient names
        """
        ingredients = []
        
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}", "")
            if ingredient and ingredient.strip():
                ingredients.append(ingredient.strip())
        
        return ingredients
    
    def extract_ingredient_items_from_meal(self, meal: dict) -> List[IngredientItem]:
        """
        Extract ingredient items with measures from meal data.
        
        Args:
            meal: Meal data from API
        
        Returns:
            List of IngredientItem objects
        """
        items = []
        
        for i in range(1, 21):
            ingredient = meal.get(f"strIngredient{i}", "")
            measure = meal.get(f"strMeasure{i}", "")
            
            if ingredient and ingredient.strip():
                items.append(IngredientItem(
                    name=ingredient.strip(),
                    quantity=measure.strip() if measure and measure.strip() else None
                ))
        
        return items
    
    def verify_meal_has_ingredients(
        self,
        meal: dict,
        required_ingredients: List[str]
    ) -> bool:
        """
        Verify that a meal contains all required ingredients.
        
        Args:
            meal: Meal data from API
            required_ingredients: List of ingredients to check for
        
        Returns:
            True if meal has all ingredients
        """
        meal_ingredients = self.extract_ingredients_from_meal(meal)
        
        for required in required_ingredients:
            # Check if this required ingredient matches any meal ingredient
            found = False
            for meal_ing in meal_ingredients:
                if ingredients_match(required, meal_ing):
                    found = True
                    break
            
            if not found:
                return False
        
        return True
    
    def meal_to_recipe(
        self,
        meal: dict,
        user_ingredients: List[str]
    ) -> Recipe:
        """
        Convert TheMealDB meal data to our Recipe model.
        
        Args:
            meal: Meal data from API
            user_ingredients: User's available ingredients
        
        Returns:
            Recipe object
        """
        # Extract all ingredients
        recipe_ingredients = self.extract_ingredients_from_meal(meal)
        ingredient_items = self.extract_ingredient_items_from_meal(meal)
        
        # Determine used vs missing
        used, missing = find_matching_ingredients(user_ingredients, recipe_ingredients)
        
        # Build category/diet list
        categories = []
        if meal.get("strCategory"):
            categories.append(meal["strCategory"])
        if meal.get("strArea"):
            categories.append(f"{meal['strArea']} cuisine")
        if meal.get("strTags"):
            # Tags are comma-separated
            tags = [t.strip() for t in meal["strTags"].split(",") if t.strip()]
            categories.extend(tags)
        
        return Recipe(
            id=meal["idMeal"],
            provider=Provider.THEMEALDB,
            title=meal.get("strMeal", "Unknown"),
            image_url=meal.get("strMealThumb"),
            source_url=meal.get("strSource") or meal.get("strYoutube"),
            ingredients=ingredient_items,
            used_ingredients=used,
            missing_ingredients=missing,
            instructions=meal.get("strInstructions"),
            servings=None,  # TheMealDB doesn't provide this
            ready_in_minutes=None,  # TheMealDB doesn't provide this
            cuisine=meal.get("strArea"),
            category_or_diet=categories,
            cost_per_serving_usd=None  # TheMealDB doesn't provide this
        )
    
    def search_by_ingredients(
        self,
        ingredients: List[str],
        max_results: int = 10
    ) -> List[Recipe]:
        """
        Search for recipes using multiple ingredients.
        
        Strategy: Find recipes that match ANY of the ingredients (more flexible).
        We'll return recipes that have at least one matching ingredient,
        sorted by how many ingredients they use.
        
        Args:
            ingredients: List of ingredient names
            max_results: Maximum number of recipes to return
        
        Returns:
            List of Recipe objects
        """
        if not ingredients:
            return []
        
        print(f"🔍 Searching TheMealDB for recipes with: {', '.join(ingredients)}")
        
        # Fast fail if API is already known to be down
        if not self.api_available:
            print("  ⚠️  TheMealDB API unavailable, using fallback recipes")
            return []
        
        # Step 1: Get candidate meal IDs for each ingredient
        all_meal_ids = set()
        meal_id_counts = {}  # Track how many ingredients each meal matches
        failed_count = 0
        
        for ingredient in ingredients:
            print(f"  → Filtering by '{ingredient}'...")
            meal_ids = self.filter_by_ingredient(ingredient)
            if meal_ids:
                print(f"    ✓ Found {len(meal_ids)} meals")
                all_meal_ids.update(meal_ids)
                # Count matches per meal
                for meal_id in meal_ids:
                    meal_id_counts[meal_id] = meal_id_counts.get(meal_id, 0) + 1
            else:
                print(f"    ⚠️  No meals found with '{ingredient}'")
                failed_count += 1
                # If all ingredients fail, stop trying (API is likely down)
                if failed_count >= len(ingredients):
                    self.api_available = False
                    break
        
        if not all_meal_ids:
            print("  ⚠️  No recipes found in TheMealDB")
            return []
        
        print(f"  ✓ Found {len(all_meal_ids)} unique meals")
        
        # Step 2: Sort meal IDs by number of matching ingredients (most matches first)
        sorted_meal_ids = sorted(
            all_meal_ids,
            key=lambda mid: meal_id_counts.get(mid, 0),
            reverse=True
        )
        
        # Step 3: Fetch details for top recipes
        recipes = []
        
        for meal_id in sorted_meal_ids[:max_results * 2]:  # Fetch extra in case some fail
            meal = self.lookup_meal(meal_id)
            
            if not meal:
                continue
            
            recipe = self.meal_to_recipe(meal, ingredients)
            recipes.append(recipe)
            
            if len(recipes) >= max_results:
                break
        
        print(f"  ✓ Fetched {len(recipes)} recipes")
        
        return recipes


def search_recipes(
    ingredients: List[str],
    max_results: int = 10,
    **kwargs
) -> List[Recipe]:
    """
    Main entry point for TheMealDB recipe search.
    
    Args:
        ingredients: List of ingredient names
        max_results: Maximum number of recipes to return
        **kwargs: Additional filters (mostly ignored for TheMealDB)
    
    Returns:
        List of Recipe objects
    """
    provider = TheMealDBProvider()
    return provider.search_by_ingredients(ingredients, max_results)

"""Recipe search orchestrator - routes to appropriate providers"""
import os
from typing import List, Optional
from core.model import Recipe
from core.normalize import parse_ingredients
from core.sorters import sort_recipes, filter_by_max_cost, filter_by_max_time

class RecipeOrchestrator:
    """Orchestrates recipe search across different providers"""
    
    def __init__(self, provider: str = "themealdb"):
        """
        Initialize orchestrator with specified provider.
        
        Args:
            provider: Provider name (themealdb, spoonacular, edamam)
        """
        self.provider = provider.lower()
    
    def search(
        self,
        ingredients: List[str],
        max_results: int = 10,
        diet: Optional[str] = None,
        health: Optional[List[str]] = None,
        max_minutes: Optional[int] = None,
        max_cost: Optional[float] = None,
        exclude: Optional[List[str]] = None,
        sort_by: str = "used-desc"
    ) -> List[Recipe]:
        """
        Search for recipes using the configured provider.
        
        Args:
            ingredients: List of ingredient names
            max_results: Maximum number of results
            diet: Dietary preference (vegetarian, vegan, etc.)
            health: Health restrictions (nut-free, dairy-free, etc.)
            max_minutes: Maximum cooking time
            max_cost: Maximum cost per serving (USD)
            exclude: Ingredients to exclude
            sort_by: How to sort results
        
        Returns:
            List of Recipe objects
        """
        if not ingredients:
            return []
        
        # Check if we should use fast mode (fallback only)
        try:
            from core.config import should_skip_api
            if should_skip_api():
                print("⚡ Fast mode: Using local recipe database")
                from providers.fallback_recipes import search_fallback_recipes
                return search_fallback_recipes(ingredients, max_results, diet, max_minutes, sort_by)
        except ImportError:
            pass  # Config not available, proceed normally
        
        # Route to appropriate provider
        if self.provider == "themealdb":
            recipes = self._search_themealdb(ingredients, max_results)
        elif self.provider == "spoonacular":
            recipes = self._search_spoonacular(
                ingredients, max_results, diet, max_minutes, max_cost, exclude
            )
        elif self.provider == "edamam":
            recipes = self._search_edamam(
                ingredients, max_results, diet, health, max_minutes, exclude
            )
        else:
            raise ValueError(f"Unknown provider: {self.provider}")
        
        # If no results, try fallback recipes
        if not recipes:
            from providers.fallback_recipes import search_fallback_recipes
            recipes = search_fallback_recipes(ingredients, max_results, diet, max_minutes, sort_by)
            # Note: Fallback recipes are already pre-filtered and sorted
            return recipes
        
        # Apply filters
        if max_cost is not None and self.provider == "spoonacular":
            recipes = filter_by_max_cost(recipes, max_cost)
        
        if max_minutes is not None:
            recipes = filter_by_max_time(recipes, max_minutes)
        
        # Sort results
        recipes = sort_recipes(recipes, sort_by)
        
        return recipes[:max_results]
    
    def _search_themealdb(
        self,
        ingredients: List[str],
        max_results: int
    ) -> List[Recipe]:
        """Search using TheMealDB provider with fast failure"""
        try:
            from providers.themealdb import search_recipes
            return search_recipes(ingredients, max_results)
        except ImportError as e:
            raise Exception(f"TheMealDB provider not available: {e}")
        except Exception as e:
            # If API fails, return empty list quickly (fallback will be used)
            print(f"TheMealDB search failed: {e}")
            return []
    
    def _search_spoonacular(
        self,
        ingredients: List[str],
        max_results: int,
        diet: Optional[str],
        max_minutes: Optional[int],
        max_cost: Optional[float],
        exclude: Optional[List[str]]
    ) -> List[Recipe]:
        """Search using Spoonacular provider"""
        # Check for API key
        api_key = os.getenv("SPOONACULAR_API_KEY")
        if not api_key or api_key == "your_spoonacular_key_here":
            raise Exception(
                "Spoonacular API key not configured. "
                "Please set SPOONACULAR_API_KEY in your .env file."
            )
        
        try:
            from providers.spoonacular import search_recipes
            return search_recipes(
                ingredients=ingredients,
                max_results=max_results,
                diet=diet,
                max_minutes=max_minutes,
                max_cost=max_cost,
                exclude=exclude,
                api_key=api_key
            )
        except ImportError as e:
            raise Exception(f"Spoonacular provider not available: {e}")
    
    def _search_edamam(
        self,
        ingredients: List[str],
        max_results: int,
        diet: Optional[str],
        health: Optional[List[str]],
        max_minutes: Optional[int],
        exclude: Optional[List[str]]
    ) -> List[Recipe]:
        """Search using Edamam provider"""
        # Check for API credentials
        app_id = os.getenv("EDAMAM_APP_ID")
        app_key = os.getenv("EDAMAM_APP_KEY")
        
        if not app_id or not app_key or \
           app_id == "your_edamam_app_id_here" or \
           app_key == "your_edamam_app_key_here":
            raise Exception(
                "Edamam API credentials not configured. "
                "Please set EDAMAM_APP_ID and EDAMAM_APP_KEY in your .env file."
            )
        
        try:
            from providers.edamam import search_recipes
            return search_recipes(
                ingredients=ingredients,
                max_results=max_results,
                diet=diet,
                health=health,
                max_minutes=max_minutes,
                exclude=exclude,
                app_id=app_id,
                app_key=app_key
            )
        except ImportError as e:
            raise Exception(f"Edamam provider not available: {e}")


def search_recipes(
    ingredients_str: str,
    provider: str = "themealdb",
    max_results: int = 10,
    diet: Optional[str] = None,
    health: Optional[List[str]] = None,
    max_minutes: Optional[int] = None,
    max_cost: Optional[float] = None,
    exclude_str: Optional[str] = None,
    sort_by: str = "used-desc"
) -> List[Recipe]:
    """
    Main entry point for recipe search.
    
    Args:
        ingredients_str: Comma-separated ingredient string
        provider: Provider to use
        max_results: Maximum number of results
        diet: Dietary preference
        health: Health restrictions
        max_minutes: Maximum cooking time
        max_cost: Maximum cost per serving
        exclude_str: Comma-separated ingredients to exclude
        sort_by: Sort method
    
    Returns:
        List of Recipe objects
    """
    # Parse ingredients
    ingredients = parse_ingredients(ingredients_str)
    exclude = parse_ingredients(exclude_str) if exclude_str else None
    
    # Create orchestrator and search
    orchestrator = RecipeOrchestrator(provider)
    return orchestrator.search(
        ingredients=ingredients,
        max_results=max_results,
        diet=diet,
        health=health,
        max_minutes=max_minutes,
        max_cost=max_cost,
        exclude=exclude,
        sort_by=sort_by
    )

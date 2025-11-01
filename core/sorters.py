"""Recipe sorting utilities"""
from typing import List
from core.model import Recipe

def sort_by_used_ingredients_desc(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by number of used ingredients (descending).
    Recipes with more user ingredients come first.
    """
    return sorted(recipes, key=lambda r: r.used_count, reverse=True)

def sort_by_missing_ingredients_asc(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by number of missing ingredients (ascending).
    Recipes with fewer missing ingredients come first.
    """
    return sorted(recipes, key=lambda r: r.missing_count)

def sort_by_cost_asc(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by cost per serving (ascending).
    Recipes without cost info go to the end.
    """
    def cost_key(recipe: Recipe):
        if recipe.cost_per_serving_usd is None:
            return float('inf')
        return recipe.cost_per_serving_usd
    
    return sorted(recipes, key=cost_key)

def sort_by_time_asc(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by cooking time (ascending).
    Recipes without time info go to the end.
    """
    def time_key(recipe: Recipe):
        if recipe.ready_in_minutes is None:
            return float('inf')
        return recipe.ready_in_minutes
    
    return sorted(recipes, key=time_key)

def sort_by_match_percentage_desc(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by ingredient match percentage (descending).
    Higher match percentage means user has more of the needed ingredients.
    """
    return sorted(recipes, key=lambda r: r.match_percentage, reverse=True)

def sort_by_relevance(recipes: List[Recipe]) -> List[Recipe]:
    """
    Sort recipes by multiple criteria for best user experience:
    1. Match percentage (highest first) - most relevant
    2. Used ingredients count (highest first) - most ingredients you have
    3. Cooking time (lowest first) - quickest to make
    
    This is the default "smart" sort.
    """
    def relevance_key(recipe: Recipe):
        # Primary: Match percentage (descending)
        match_pct = recipe.match_percentage
        
        # Secondary: Used ingredients count (descending)
        used_count = recipe.used_count
        
        # Tertiary: Cooking time (ascending, None = high value)
        time = recipe.ready_in_minutes if recipe.ready_in_minutes is not None else 999999
        
        # Return tuple for multi-level sort
        # Negative for descending order
        return (-match_pct, -used_count, time)
    
    return sorted(recipes, key=relevance_key)

def sort_recipes(recipes: List[Recipe], sort_by: str) -> List[Recipe]:
    """
    Sort recipes according to the specified method.
    
    Args:
        recipes: List of recipes to sort
        sort_by: Sorting method
            - 'used-desc': Most used ingredients first
            - 'missing-asc': Fewest missing ingredients first
            - 'cost-asc': Lowest cost first
            - 'time-asc': Shortest time first
            - 'match-desc': Best match percentage first
            - 'relevance': Smart sort (match % → used count → time) [DEFAULT]
    
    Returns:
        Sorted list of recipes
    """
    if not recipes:
        return recipes
    
    if sort_by == 'used-desc':
        return sort_by_used_ingredients_desc(recipes)
    elif sort_by == 'missing-asc':
        return sort_by_missing_ingredients_asc(recipes)
    elif sort_by == 'cost-asc':
        return sort_by_cost_asc(recipes)
    elif sort_by == 'time-asc':
        return sort_by_time_asc(recipes)
    elif sort_by == 'match-desc':
        return sort_by_match_percentage_desc(recipes)
    elif sort_by == 'relevance':
        return sort_by_relevance(recipes)
    else:
        # Default: smart relevance sort (match → used → time)
        return sort_by_relevance(recipes)

def filter_by_max_cost(recipes: List[Recipe], max_cost: float) -> List[Recipe]:
    """
    Filter recipes by maximum cost per serving.
    
    Args:
        recipes: List of recipes
        max_cost: Maximum cost per serving in USD
    
    Returns:
        Filtered list
    """
    return [
        r for r in recipes
        if r.cost_per_serving_usd is not None and r.cost_per_serving_usd <= max_cost
    ]

def filter_by_max_time(recipes: List[Recipe], max_minutes: int) -> List[Recipe]:
    """
    Filter recipes by maximum cooking time.
    
    Args:
        recipes: List of recipes
        max_minutes: Maximum cooking time in minutes
    
    Returns:
        Filtered list
    """
    return [
        r for r in recipes
        if r.ready_in_minutes is not None and r.ready_in_minutes <= max_minutes
    ]

"""Ingredient normalization utilities"""
import re
from typing import List, Set
from core.performance import memoize

@memoize
def parse_ingredients(ingredients_str: str) -> List[str]:
    """
    Parse comma/space separated ingredient string into normalized list.
    
    Args:
        ingredients_str: Raw ingredient string (e.g., "egg, tomato,   onion")
    
    Returns:
        List of normalized ingredient names
    """
    if not ingredients_str:
        return []
    
    # Split by comma or semicolon
    parts = re.split(r'[,;]', ingredients_str)
    
    normalized = []
    seen = set()
    
    for part in parts:
        # Clean whitespace
        ingredient = part.strip().lower()
        
        if not ingredient:
            continue
        
        # Remove extra spaces
        ingredient = re.sub(r'\s+', ' ', ingredient)
        
        # Skip duplicates
        if ingredient in seen:
            continue
        
        seen.add(ingredient)
        normalized.append(ingredient)
    
    return normalized

def normalize_for_themealdb(ingredient: str) -> str:
    """
    Normalize ingredient for TheMealDB API (spaces to underscores).
    
    Args:
        ingredient: Ingredient name (e.g., "chicken breast")
    
    Returns:
        Normalized name (e.g., "chicken_breast")
    """
    return ingredient.replace(' ', '_')

def normalize_ingredient_name(name: str) -> str:
    """
    Normalize ingredient name for comparison (lowercase, no extra spaces).
    
    Args:
        name: Raw ingredient name
    
    Returns:
        Normalized name
    """
    if not name:
        return ""
    
    # Convert to lowercase and strip
    name = name.strip().lower()
    
    # Remove extra whitespace
    name = re.sub(r'\s+', ' ', name)
    
    return name

@memoize
def ingredients_match(ing1: str, ing2: str) -> bool:
    """
    Check if two ingredient names match (fuzzy matching).
    Memoized for performance (called frequently in loops).
    
    Args:
        ing1: First ingredient name
        ing2: Second ingredient name
    
    Returns:
        True if ingredients match
    """
    norm1 = normalize_ingredient_name(ing1)
    norm2 = normalize_ingredient_name(ing2)
    
    # Exact match
    if norm1 == norm2:
        return True
    
    # One contains the other (e.g., "egg" matches "eggs")
    if norm1 in norm2 or norm2 in norm1:
        return True
    
    # Handle plurals
    if norm1.rstrip('s') == norm2.rstrip('s'):
        return True
    
    return False

def find_matching_ingredients(
    user_ingredients: List[str],
    recipe_ingredients: List[str]
) -> tuple[List[str], List[str]]:
    """
    Separate recipe ingredients into used and missing based on user's ingredients.
    
    Args:
        user_ingredients: Ingredients the user has
        recipe_ingredients: All ingredients in the recipe
    
    Returns:
        Tuple of (used_ingredients, missing_ingredients)
    """
    used = []
    missing = []
    
    # Normalize user ingredients for comparison
    user_normalized = {normalize_ingredient_name(ing) for ing in user_ingredients}
    
    for recipe_ing in recipe_ingredients:
        recipe_norm = normalize_ingredient_name(recipe_ing)
        
        # Check if any user ingredient matches this recipe ingredient
        matched = False
        for user_ing in user_ingredients:
            if ingredients_match(user_ing, recipe_ing):
                used.append(recipe_ing)
                matched = True
                break
        
        if not matched:
            missing.append(recipe_ing)
    
    return used, missing

def deduplicate_ingredients(ingredients: List[str]) -> List[str]:
    """
    Remove duplicate ingredients while preserving order.
    
    Args:
        ingredients: List of ingredient names
    
    Returns:
        Deduplicated list
    """
    seen = set()
    result = []
    
    for ing in ingredients:
        norm = normalize_ingredient_name(ing)
        if norm not in seen and norm:
            seen.add(norm)
            result.append(ing)
    
    return result

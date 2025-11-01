"""Data models for the recipe finder"""
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class Provider(Enum):
    """Supported API providers"""
    THEMEALDB = "themealdb"
    SPOONACULAR = "spoonacular"
    EDAMAM = "edamam"

@dataclass
class IngredientItem:
    """Single ingredient with optional quantity/unit"""
    name: str
    quantity: Optional[str] = None
    unit: Optional[str] = None
    
    def __str__(self):
        if self.quantity and self.unit:
            return f"{self.quantity} {self.unit} {self.name}"
        elif self.quantity:
            return f"{self.quantity} {self.name}"
        return self.name

@dataclass
class Recipe:
    """Normalized recipe model across all providers"""
    id: str
    provider: Provider
    title: str
    image_url: Optional[str] = None
    source_url: Optional[str] = None
    ingredients: List[IngredientItem] = field(default_factory=list)
    used_ingredients: List[str] = field(default_factory=list)
    missing_ingredients: List[str] = field(default_factory=list)
    instructions: Optional[str] = None
    servings: Optional[int] = None
    ready_in_minutes: Optional[int] = None
    cuisine: Optional[str] = None
    category_or_diet: List[str] = field(default_factory=list)
    cost_per_serving_usd: Optional[float] = None
    
    @property
    def used_count(self) -> int:
        """Number of user ingredients used in this recipe"""
        return len(self.used_ingredients)
    
    @property
    def missing_count(self) -> int:
        """Number of additional ingredients needed"""
        return len(self.missing_ingredients)
    
    @property
    def match_percentage(self) -> float:
        """Percentage of recipe ingredients user has (0-100)"""
        total = self.used_count + self.missing_count
        if total == 0:
            return 0.0
        return (self.used_count / total) * 100
    
    def to_dict(self) -> dict:
        """Convert recipe to dictionary for export"""
        return {
            'id': self.id,
            'provider': self.provider.value,
            'title': self.title,
            'image_url': self.image_url,
            'source_url': self.source_url,
            'ingredients': [str(ing) for ing in self.ingredients],
            'used_ingredients': self.used_ingredients,
            'missing_ingredients': self.missing_ingredients,
            'instructions': self.instructions,
            'servings': self.servings,
            'ready_in_minutes': self.ready_in_minutes,
            'cuisine': self.cuisine,
            'category_or_diet': self.category_or_diet,
            'cost_per_serving_usd': self.cost_per_serving_usd,
            'match_percentage': round(self.match_percentage, 1)
        }

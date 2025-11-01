"""Tests for recipe sorting"""
import unittest
from core.model import Recipe, Provider
from core.sorters import (
    sort_by_used_ingredients_desc,
    sort_by_missing_ingredients_asc,
    sort_by_cost_asc,
    sort_by_time_asc,
    filter_by_max_cost,
    filter_by_max_time
)

class TestSorters(unittest.TestCase):
    """Test recipe sorting functions"""
    
    def setUp(self):
        """Set up test recipes"""
        self.recipe1 = Recipe(
            id="1",
            provider=Provider.THEMEALDB,
            title="Recipe 1",
            used_ingredients=["egg", "tomato"],
            missing_ingredients=["onion"],
            cost_per_serving_usd=2.50,
            ready_in_minutes=30
        )
        
        self.recipe2 = Recipe(
            id="2",
            provider=Provider.THEMEALDB,
            title="Recipe 2",
            used_ingredients=["egg"],
            missing_ingredients=["tomato", "onion", "pepper"],
            cost_per_serving_usd=1.50,
            ready_in_minutes=45
        )
        
        self.recipe3 = Recipe(
            id="3",
            provider=Provider.THEMEALDB,
            title="Recipe 3",
            used_ingredients=["egg", "tomato", "onion"],
            missing_ingredients=[],
            cost_per_serving_usd=3.00,
            ready_in_minutes=20
        )
    
    def test_sort_by_used_desc(self):
        """Test sorting by used ingredients (descending)"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        sorted_recipes = sort_by_used_ingredients_desc(recipes)
        
        # Recipe 3 has most used (3), then Recipe 1 (2), then Recipe 2 (1)
        self.assertEqual(sorted_recipes[0].id, "3")
        self.assertEqual(sorted_recipes[1].id, "1")
        self.assertEqual(sorted_recipes[2].id, "2")
    
    def test_sort_by_missing_asc(self):
        """Test sorting by missing ingredients (ascending)"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        sorted_recipes = sort_by_missing_ingredients_asc(recipes)
        
        # Recipe 3 has 0 missing, Recipe 1 has 1, Recipe 2 has 3
        self.assertEqual(sorted_recipes[0].id, "3")
        self.assertEqual(sorted_recipes[1].id, "1")
        self.assertEqual(sorted_recipes[2].id, "2")
    
    def test_sort_by_cost_asc(self):
        """Test sorting by cost (ascending)"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        sorted_recipes = sort_by_cost_asc(recipes)
        
        # Recipe 2 ($1.50), Recipe 1 ($2.50), Recipe 3 ($3.00)
        self.assertEqual(sorted_recipes[0].id, "2")
        self.assertEqual(sorted_recipes[1].id, "1")
        self.assertEqual(sorted_recipes[2].id, "3")
    
    def test_sort_by_time_asc(self):
        """Test sorting by time (ascending)"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        sorted_recipes = sort_by_time_asc(recipes)
        
        # Recipe 3 (20m), Recipe 1 (30m), Recipe 2 (45m)
        self.assertEqual(sorted_recipes[0].id, "3")
        self.assertEqual(sorted_recipes[1].id, "1")
        self.assertEqual(sorted_recipes[2].id, "2")
    
    def test_filter_by_max_cost(self):
        """Test filtering by maximum cost"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        filtered = filter_by_max_cost(recipes, 2.00)
        
        # Only Recipe 2 ($1.50) should pass
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].id, "2")
    
    def test_filter_by_max_time(self):
        """Test filtering by maximum time"""
        recipes = [self.recipe1, self.recipe2, self.recipe3]
        filtered = filter_by_max_time(recipes, 30)
        
        # Recipe 3 (20m) and Recipe 1 (30m) should pass
        self.assertEqual(len(filtered), 2)
        ids = {r.id for r in filtered}
        self.assertIn("1", ids)
        self.assertIn("3", ids)

if __name__ == '__main__':
    unittest.main()

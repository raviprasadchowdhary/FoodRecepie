"""Tests for ingredient normalization"""
import unittest
from core.normalize import (
    parse_ingredients,
    normalize_for_themealdb,
    normalize_ingredient_name,
    ingredients_match,
    find_matching_ingredients,
    deduplicate_ingredients
)

class TestParseIngredients(unittest.TestCase):
    """Test ingredient parsing"""
    
    def test_comma_separated(self):
        """Test parsing comma-separated ingredients"""
        result = parse_ingredients("egg, tomato, onion")
        self.assertEqual(result, ["egg", "tomato", "onion"])
    
    def test_mixed_whitespace(self):
        """Test parsing with mixed whitespace"""
        result = parse_ingredients("egg,  tomato ,onion")
        self.assertEqual(result, ["egg", "tomato", "onion"])
    
    def test_duplicate_removal(self):
        """Test that duplicates are removed"""
        result = parse_ingredients("egg, tomato, egg")
        self.assertEqual(result, ["egg", "tomato"])
    
    def test_empty_input(self):
        """Test empty input"""
        result = parse_ingredients("")
        self.assertEqual(result, [])
    
    def test_case_normalization(self):
        """Test case normalization"""
        result = parse_ingredients("Egg, TOMATO, Onion")
        self.assertEqual(result, ["egg", "tomato", "onion"])

class TestNormalizeForTheMealDB(unittest.TestCase):
    """Test TheMealDB normalization"""
    
    def test_spaces_to_underscores(self):
        """Test converting spaces to underscores"""
        result = normalize_for_themealdb("chicken breast")
        self.assertEqual(result, "chicken_breast")
    
    def test_single_word(self):
        """Test single word ingredient"""
        result = normalize_for_themealdb("chicken")
        self.assertEqual(result, "chicken")

class TestIngredientsMatch(unittest.TestCase):
    """Test ingredient matching logic"""
    
    def test_exact_match(self):
        """Test exact match"""
        self.assertTrue(ingredients_match("egg", "egg"))
    
    def test_case_insensitive(self):
        """Test case insensitive match"""
        self.assertTrue(ingredients_match("Egg", "egg"))
    
    def test_plural_match(self):
        """Test plural matching"""
        self.assertTrue(ingredients_match("egg", "eggs"))
        self.assertTrue(ingredients_match("tomato", "tomatoes"))
    
    def test_substring_match(self):
        """Test substring matching"""
        self.assertTrue(ingredients_match("chicken", "chicken breast"))
    
    def test_no_match(self):
        """Test non-matching ingredients"""
        self.assertFalse(ingredients_match("egg", "tomato"))

class TestFindMatchingIngredients(unittest.TestCase):
    """Test finding used vs missing ingredients"""
    
    def test_all_used(self):
        """Test when user has all ingredients"""
        user = ["egg", "tomato"]
        recipe = ["egg", "tomato"]
        used, missing = find_matching_ingredients(user, recipe)
        
        self.assertEqual(len(used), 2)
        self.assertEqual(len(missing), 0)
    
    def test_some_missing(self):
        """Test when user is missing some ingredients"""
        user = ["egg"]
        recipe = ["egg", "tomato", "onion"]
        used, missing = find_matching_ingredients(user, recipe)
        
        self.assertEqual(len(used), 1)
        self.assertEqual(len(missing), 2)
        self.assertIn("egg", used)
        self.assertIn("tomato", missing)
        self.assertIn("onion", missing)
    
    def test_plural_matching(self):
        """Test plural matching in used/missing"""
        user = ["egg"]
        recipe = ["eggs", "tomato"]
        used, missing = find_matching_ingredients(user, recipe)
        
        self.assertEqual(len(used), 1)
        self.assertIn("eggs", used)

class TestDeduplicateIngredients(unittest.TestCase):
    """Test ingredient deduplication"""
    
    def test_removes_duplicates(self):
        """Test duplicate removal"""
        result = deduplicate_ingredients(["egg", "tomato", "egg"])
        self.assertEqual(result, ["egg", "tomato"])
    
    def test_preserves_order(self):
        """Test order preservation"""
        result = deduplicate_ingredients(["tomato", "egg", "onion"])
        self.assertEqual(result, ["tomato", "egg", "onion"])
    
    def test_empty_list(self):
        """Test empty list"""
        result = deduplicate_ingredients([])
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

"""
Fallback recipe database with common recipes from around the world
Used when API providers return no results
"""

from core.model import Recipe, Provider, IngredientItem
from typing import List

# Database of common recipes with ingredients
FALLBACK_RECIPES = [
    # Indian Recipes
    {
        "id": "fallback_001",
        "title": "Simple Dal (Indian Lentils)",
        "cuisine": "Indian",
        "category": ["Vegetarian", "Vegan", "Budget-friendly"],
        "ingredients": ["lentils", "onion", "tomato", "garlic", "ginger", "cumin", "turmeric", "salt"],
        "time": 30,
        "servings": 4,
        "instructions": "A simple Indian lentil dish perfect with rice or bread."
    },
    {
        "id": "fallback_002",
        "title": "Egg Curry",
        "cuisine": "Indian",
        "category": ["Protein-rich"],
        "ingredients": ["eggs", "onion", "tomato", "garlic", "ginger", "curry powder", "oil", "salt"],
        "time": 25,
        "servings": 4,
        "instructions": "Boiled eggs in a flavorful curry sauce."
    },
    {
        "id": "fallback_003",
        "title": "Vegetable Biryani",
        "cuisine": "Indian",
        "category": ["Vegetarian", "One-pot"],
        "ingredients": ["rice", "mixed vegetables", "onion", "yogurt", "spices", "oil"],
        "time": 45,
        "servings": 6,
        "instructions": "Fragrant rice with mixed vegetables and aromatic spices."
    },
    {
        "id": "fallback_004",
        "title": "Paneer Tikka",
        "cuisine": "Indian",
        "category": ["Vegetarian", "Grilled"],
        "ingredients": ["paneer", "yogurt", "bell pepper", "onion", "spices", "lemon"],
        "time": 30,
        "servings": 4,
        "instructions": "Grilled cottage cheese with vegetables."
    },
    {
        "id": "fallback_005",
        "title": "Chicken Tikka Masala",
        "cuisine": "Indian",
        "category": ["Popular", "Curry"],
        "ingredients": ["chicken", "cream", "tomato", "onion", "garlic", "ginger", "spices"],
        "time": 40,
        "servings": 4,
        "instructions": "Creamy tomato-based chicken curry."
    },
    
    # American Recipes
    {
        "id": "fallback_006",
        "title": "Classic Cheeseburger",
        "cuisine": "American",
        "category": ["Fast food", "Popular"],
        "ingredients": ["ground beef", "cheese", "burger buns", "lettuce", "tomato", "onion", "pickles"],
        "time": 20,
        "servings": 4,
        "instructions": "All-American classic burger."
    },
    {
        "id": "fallback_007",
        "title": "Mac and Cheese",
        "cuisine": "American",
        "category": ["Comfort food", "Kid-friendly"],
        "ingredients": ["pasta", "cheese", "milk", "butter", "flour"],
        "time": 25,
        "servings": 4,
        "instructions": "Creamy, cheesy pasta comfort food."
    },
    {
        "id": "fallback_008",
        "title": "Scrambled Eggs and Toast",
        "cuisine": "American",
        "category": ["Breakfast", "Quick"],
        "ingredients": ["eggs", "bread", "butter", "milk", "salt", "pepper"],
        "time": 10,
        "servings": 2,
        "instructions": "Simple American breakfast."
    },
    {
        "id": "fallback_009",
        "title": "Grilled Cheese Sandwich",
        "cuisine": "American",
        "category": ["Quick", "Comfort food"],
        "ingredients": ["bread", "cheese", "butter"],
        "time": 10,
        "servings": 1,
        "instructions": "Classic grilled cheese."
    },
    {
        "id": "fallback_010",
        "title": "BBQ Chicken Wings",
        "cuisine": "American",
        "category": ["BBQ", "Party food"],
        "ingredients": ["chicken wings", "bbq sauce", "oil", "garlic powder", "salt"],
        "time": 35,
        "servings": 4,
        "instructions": "Crispy wings with BBQ sauce."
    },
    
    # British Recipes
    {
        "id": "fallback_011",
        "title": "Beans on Toast",
        "cuisine": "British",
        "category": ["Quick", "Budget-friendly"],
        "ingredients": ["baked beans", "bread", "butter"],
        "time": 5,
        "servings": 1,
        "instructions": "Classic British quick meal."
    },
    {
        "id": "fallback_012",
        "title": "Fish and Chips",
        "cuisine": "British",
        "category": ["Traditional", "Popular"],
        "ingredients": ["fish", "potatoes", "flour", "oil", "salt", "vinegar"],
        "time": 40,
        "servings": 4,
        "instructions": "Iconic British dish."
    },
    {
        "id": "fallback_013",
        "title": "Shepherd's Pie",
        "cuisine": "British",
        "category": ["Comfort food", "One-dish"],
        "ingredients": ["ground lamb", "potatoes", "carrots", "peas", "onion", "gravy"],
        "time": 60,
        "servings": 6,
        "instructions": "Hearty meat and potato pie."
    },
    {
        "id": "fallback_014",
        "title": "English Breakfast",
        "cuisine": "British",
        "category": ["Breakfast", "Hearty"],
        "ingredients": ["eggs", "bacon", "sausage", "beans", "toast", "tomato", "mushrooms"],
        "time": 25,
        "servings": 2,
        "instructions": "Full English breakfast."
    },
    
    # Mexican Recipes
    {
        "id": "fallback_015",
        "title": "Chicken Tacos",
        "cuisine": "Mexican",
        "category": ["Popular", "Quick"],
        "ingredients": ["chicken", "tortillas", "lettuce", "tomato", "cheese", "salsa", "lime"],
        "time": 20,
        "servings": 4,
        "instructions": "Simple and delicious tacos."
    },
    {
        "id": "fallback_016",
        "title": "Quesadillas",
        "cuisine": "Mexican",
        "category": ["Quick", "Cheese"],
        "ingredients": ["tortillas", "cheese", "beans", "onion", "peppers"],
        "time": 15,
        "servings": 2,
        "instructions": "Cheesy grilled tortillas."
    },
    {
        "id": "fallback_017",
        "title": "Guacamole",
        "cuisine": "Mexican",
        "category": ["Appetizer", "Vegan"],
        "ingredients": ["avocado", "lime", "tomato", "onion", "cilantro", "salt"],
        "time": 10,
        "servings": 4,
        "instructions": "Fresh avocado dip."
    },
    {
        "id": "fallback_018",
        "title": "Bean Burritos",
        "cuisine": "Mexican",
        "category": ["Vegetarian", "Filling"],
        "ingredients": ["tortillas", "beans", "rice", "cheese", "salsa", "sour cream"],
        "time": 20,
        "servings": 4,
        "instructions": "Hearty bean-filled burritos."
    },
    {
        "id": "fallback_019",
        "title": "Chicken Enchiladas",
        "cuisine": "Mexican",
        "category": ["Baked", "Cheese"],
        "ingredients": ["chicken", "tortillas", "enchilada sauce", "cheese", "onion", "cream"],
        "time": 45,
        "servings": 6,
        "instructions": "Baked tortillas with chicken and cheese."
    },
    
    # Italian Recipes
    {
        "id": "fallback_020",
        "title": "Spaghetti Carbonara",
        "cuisine": "Italian",
        "category": ["Pasta", "Quick"],
        "ingredients": ["spaghetti", "bacon", "eggs", "parmesan cheese", "black pepper"],
        "time": 20,
        "servings": 4,
        "instructions": "Classic Roman pasta dish."
    },
    {
        "id": "fallback_021",
        "title": "Margherita Pizza",
        "cuisine": "Italian",
        "category": ["Pizza", "Vegetarian"],
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil", "olive oil"],
        "time": 25,
        "servings": 2,
        "instructions": "Simple Italian pizza."
    },
    {
        "id": "fallback_022",
        "title": "Pasta Aglio e Olio",
        "cuisine": "Italian",
        "category": ["Pasta", "Quick", "Vegan"],
        "ingredients": ["spaghetti", "garlic", "olive oil", "red pepper flakes", "parsley"],
        "time": 15,
        "servings": 4,
        "instructions": "Simple garlic and oil pasta."
    },
    {
        "id": "fallback_023",
        "title": "Lasagna",
        "cuisine": "Italian",
        "category": ["Baked", "Comfort food"],
        "ingredients": ["lasagna noodles", "ground beef", "tomato sauce", "ricotta", "mozzarella", "parmesan"],
        "time": 90,
        "servings": 8,
        "instructions": "Layered pasta bake."
    },
    
    # Chinese Recipes
    {
        "id": "fallback_024",
        "title": "Fried Rice",
        "cuisine": "Chinese",
        "category": ["Quick", "One-pan"],
        "ingredients": ["rice", "eggs", "vegetables", "soy sauce", "oil", "garlic"],
        "time": 15,
        "servings": 4,
        "instructions": "Classic Chinese fried rice."
    },
    {
        "id": "fallback_025",
        "title": "Egg Drop Soup",
        "cuisine": "Chinese",
        "category": ["Soup", "Light"],
        "ingredients": ["eggs", "chicken broth", "cornstarch", "green onions", "soy sauce"],
        "time": 15,
        "servings": 4,
        "instructions": "Simple Chinese soup."
    },
    {
        "id": "fallback_026",
        "title": "Stir-Fry Vegetables",
        "cuisine": "Chinese",
        "category": ["Vegetarian", "Quick"],
        "ingredients": ["mixed vegetables", "soy sauce", "garlic", "ginger", "oil"],
        "time": 15,
        "servings": 4,
        "instructions": "Quick vegetable stir-fry."
    },
    
    # Japanese Recipes
    {
        "id": "fallback_027",
        "title": "Miso Soup",
        "cuisine": "Japanese",
        "category": ["Soup", "Light"],
        "ingredients": ["miso paste", "tofu", "seaweed", "green onions", "water"],
        "time": 10,
        "servings": 4,
        "instructions": "Traditional Japanese soup."
    },
    {
        "id": "fallback_028",
        "title": "Teriyaki Chicken",
        "cuisine": "Japanese",
        "category": ["Grilled", "Sweet"],
        "ingredients": ["chicken", "soy sauce", "mirin", "sugar", "ginger", "garlic"],
        "time": 30,
        "servings": 4,
        "instructions": "Sweet glazed chicken."
    },
    
    # Middle Eastern Recipes
    {
        "id": "fallback_029",
        "title": "Hummus",
        "cuisine": "Middle Eastern",
        "category": ["Vegan", "Appetizer"],
        "ingredients": ["chickpeas", "tahini", "lemon", "garlic", "olive oil", "salt"],
        "time": 10,
        "servings": 6,
        "instructions": "Creamy chickpea dip."
    },
    {
        "id": "fallback_030",
        "title": "Falafel",
        "cuisine": "Middle Eastern",
        "category": ["Vegan", "Fried"],
        "ingredients": ["chickpeas", "onion", "garlic", "parsley", "cumin", "flour"],
        "time": 30,
        "servings": 4,
        "instructions": "Crispy chickpea fritters."
    },
    
    # Universal/Simple Recipes
    {
        "id": "fallback_031",
        "title": "Omelette",
        "cuisine": "Universal",
        "category": ["Breakfast", "Quick"],
        "ingredients": ["eggs", "cheese", "vegetables", "salt", "pepper", "butter"],
        "time": 10,
        "servings": 1,
        "instructions": "Simple egg omelette."
    },
    {
        "id": "fallback_032",
        "title": "Grilled Chicken Salad",
        "cuisine": "Universal",
        "category": ["Healthy", "Salad"],
        "ingredients": ["chicken", "lettuce", "tomato", "cucumber", "dressing", "croutons"],
        "time": 20,
        "servings": 2,
        "instructions": "Healthy grilled chicken salad."
    },
    {
        "id": "fallback_033",
        "title": "Vegetable Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Healthy", "Vegetarian"],
        "ingredients": ["mixed vegetables", "vegetable broth", "onion", "garlic", "herbs"],
        "time": 30,
        "servings": 6,
        "instructions": "Healthy vegetable soup."
    },
    {
        "id": "fallback_034",
        "title": "Tuna Sandwich",
        "cuisine": "Universal",
        "category": ["Quick", "Lunch"],
        "ingredients": ["tuna", "bread", "mayonnaise", "lettuce", "tomato"],
        "time": 10,
        "servings": 1,
        "instructions": "Simple tuna sandwich."
    },
    {
        "id": "fallback_035",
        "title": "Pancakes",
        "cuisine": "Universal",
        "category": ["Breakfast", "Sweet"],
        "ingredients": ["flour", "eggs", "milk", "sugar", "butter", "baking powder"],
        "time": 20,
        "servings": 4,
        "instructions": "Fluffy breakfast pancakes."
    },
    {
        "id": "fallback_036",
        "title": "Caesar Salad",
        "cuisine": "Universal",
        "category": ["Salad", "Quick"],
        "ingredients": ["lettuce", "croutons", "parmesan", "caesar dressing", "lemon"],
        "time": 10,
        "servings": 2,
        "instructions": "Classic Caesar salad."
    },
    {
        "id": "fallback_037",
        "title": "Tomato Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Comfort food"],
        "ingredients": ["tomatoes", "onion", "garlic", "cream", "basil", "broth"],
        "time": 30,
        "servings": 4,
        "instructions": "Creamy tomato soup."
    },
    {
        "id": "fallback_038",
        "title": "Chicken Noodle Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Comfort food"],
        "ingredients": ["chicken", "noodles", "carrots", "celery", "onion", "broth"],
        "time": 40,
        "servings": 6,
        "instructions": "Classic chicken soup."
    },
    {
        "id": "fallback_039",
        "title": "BLT Sandwich",
        "cuisine": "American",
        "category": ["Sandwich", "Quick"],
        "ingredients": ["bacon", "lettuce", "tomato", "bread", "mayonnaise"],
        "time": 15,
        "servings": 1,
        "instructions": "Bacon, lettuce, and tomato sandwich."
    },
    {
        "id": "fallback_040",
        "title": "French Toast",
        "cuisine": "French",
        "category": ["Breakfast", "Sweet"],
        "ingredients": ["bread", "eggs", "milk", "cinnamon", "butter", "syrup"],
        "time": 15,
        "servings": 2,
        "instructions": "Sweet breakfast bread."
    },
    
    # Thai Recipes
    {
        "id": "fallback_041",
        "title": "Pad Thai",
        "cuisine": "Thai",
        "category": ["Noodles", "Popular"],
        "ingredients": ["rice noodles", "shrimp", "eggs", "peanuts", "bean sprouts", "lime", "fish sauce"],
        "time": 25,
        "servings": 4,
        "instructions": "Classic Thai stir-fried noodles."
    },
    {
        "id": "fallback_042",
        "title": "Thai Green Curry",
        "cuisine": "Thai",
        "category": ["Curry", "Spicy"],
        "ingredients": ["chicken", "coconut milk", "green curry paste", "vegetables", "basil", "fish sauce"],
        "time": 30,
        "servings": 4,
        "instructions": "Aromatic Thai curry with coconut milk."
    },
    {
        "id": "fallback_043",
        "title": "Tom Yum Soup",
        "cuisine": "Thai",
        "category": ["Soup", "Spicy"],
        "ingredients": ["shrimp", "mushrooms", "lemongrass", "lime", "chili", "fish sauce", "broth"],
        "time": 20,
        "servings": 4,
        "instructions": "Spicy and sour Thai soup."
    },
    
    # Korean Recipes
    {
        "id": "fallback_044",
        "title": "Kimchi Fried Rice",
        "cuisine": "Korean",
        "category": ["Rice", "Spicy"],
        "ingredients": ["rice", "kimchi", "eggs", "gochujang", "sesame oil", "green onions"],
        "time": 15,
        "servings": 2,
        "instructions": "Spicy Korean fried rice with kimchi."
    },
    {
        "id": "fallback_045",
        "title": "Bibimbap",
        "cuisine": "Korean",
        "category": ["Rice bowl", "Healthy"],
        "ingredients": ["rice", "vegetables", "beef", "egg", "gochujang", "sesame oil"],
        "time": 30,
        "servings": 4,
        "instructions": "Mixed rice bowl with vegetables and meat."
    },
    {
        "id": "fallback_046",
        "title": "Korean Beef Bulgogi",
        "cuisine": "Korean",
        "category": ["Grilled", "Marinated"],
        "ingredients": ["beef", "soy sauce", "sugar", "garlic", "sesame oil", "pear", "green onions"],
        "time": 35,
        "servings": 4,
        "instructions": "Sweet and savory marinated beef."
    },
    
    # Vietnamese Recipes
    {
        "id": "fallback_047",
        "title": "Pho (Vietnamese Soup)",
        "cuisine": "Vietnamese",
        "category": ["Soup", "Noodles"],
        "ingredients": ["rice noodles", "beef", "broth", "bean sprouts", "basil", "lime", "onion"],
        "time": 60,
        "servings": 4,
        "instructions": "Aromatic Vietnamese noodle soup."
    },
    {
        "id": "fallback_048",
        "title": "Banh Mi Sandwich",
        "cuisine": "Vietnamese",
        "category": ["Sandwich", "Fusion"],
        "ingredients": ["baguette", "pork", "pickled vegetables", "cilantro", "mayonnaise", "jalapeño"],
        "time": 20,
        "servings": 2,
        "instructions": "Vietnamese-French fusion sandwich."
    },
    {
        "id": "fallback_049",
        "title": "Vietnamese Spring Rolls",
        "cuisine": "Vietnamese",
        "category": ["Appetizer", "Healthy"],
        "ingredients": ["rice paper", "shrimp", "lettuce", "rice noodles", "mint", "peanut sauce"],
        "time": 25,
        "servings": 4,
        "instructions": "Fresh spring rolls with peanut sauce."
    },
    
    # Spanish Recipes
    {
        "id": "fallback_050",
        "title": "Spanish Omelette (Tortilla)",
        "cuisine": "Spanish",
        "category": ["Eggs", "Traditional"],
        "ingredients": ["potatoes", "eggs", "onion", "olive oil", "salt"],
        "time": 30,
        "servings": 4,
        "instructions": "Traditional Spanish potato omelette."
    },
    {
        "id": "fallback_051",
        "title": "Paella",
        "cuisine": "Spanish",
        "category": ["Rice", "Seafood"],
        "ingredients": ["rice", "chicken", "shrimp", "saffron", "peas", "bell peppers", "broth"],
        "time": 50,
        "servings": 6,
        "instructions": "Spanish rice dish with seafood and chicken."
    },
    {
        "id": "fallback_052",
        "title": "Gazpacho",
        "cuisine": "Spanish",
        "category": ["Soup", "Cold", "Vegan"],
        "ingredients": ["tomatoes", "cucumber", "bell pepper", "garlic", "olive oil", "vinegar", "bread"],
        "time": 15,
        "servings": 4,
        "instructions": "Cold Spanish tomato soup."
    },
    
    # Greek Recipes
    {
        "id": "fallback_053",
        "title": "Greek Salad",
        "cuisine": "Greek",
        "category": ["Salad", "Vegetarian"],
        "ingredients": ["tomatoes", "cucumber", "feta cheese", "olives", "onion", "olive oil", "oregano"],
        "time": 10,
        "servings": 4,
        "instructions": "Fresh Mediterranean salad."
    },
    {
        "id": "fallback_054",
        "title": "Moussaka",
        "cuisine": "Greek",
        "category": ["Baked", "Comfort food"],
        "ingredients": ["eggplant", "ground beef", "potatoes", "béchamel sauce", "tomatoes", "onion"],
        "time": 90,
        "servings": 8,
        "instructions": "Layered eggplant casserole."
    },
    {
        "id": "fallback_055",
        "title": "Tzatziki Sauce",
        "cuisine": "Greek",
        "category": ["Sauce", "Vegetarian"],
        "ingredients": ["yogurt", "cucumber", "garlic", "dill", "lemon", "olive oil"],
        "time": 10,
        "servings": 6,
        "instructions": "Creamy Greek yogurt and cucumber sauce."
    },
    {
        "id": "fallback_056",
        "title": "Gyros",
        "cuisine": "Greek",
        "category": ["Sandwich", "Grilled"],
        "ingredients": ["pork", "pita bread", "tzatziki", "tomatoes", "onion", "lettuce"],
        "time": 30,
        "servings": 4,
        "instructions": "Greek grilled meat sandwich."
    },
    
    # More American Comfort Food
    {
        "id": "fallback_057",
        "title": "Chicken Pot Pie",
        "cuisine": "American",
        "category": ["Pie", "Comfort food"],
        "ingredients": ["chicken", "mixed vegetables", "cream", "pie crust", "butter", "broth"],
        "time": 60,
        "servings": 6,
        "instructions": "Creamy chicken and vegetable pie."
    },
    {
        "id": "fallback_058",
        "title": "Meatloaf",
        "cuisine": "American",
        "category": ["Baked", "Comfort food"],
        "ingredients": ["ground beef", "breadcrumbs", "eggs", "onion", "ketchup", "worcestershire sauce"],
        "time": 60,
        "servings": 6,
        "instructions": "Classic American meatloaf."
    },
    {
        "id": "fallback_059",
        "title": "Chicken Fried Rice",
        "cuisine": "American-Chinese",
        "category": ["Rice", "One-pan"],
        "ingredients": ["rice", "chicken", "eggs", "vegetables", "soy sauce", "garlic"],
        "time": 20,
        "servings": 4,
        "instructions": "American-style chicken fried rice."
    },
    {
        "id": "fallback_060",
        "title": "Coleslaw",
        "cuisine": "American",
        "category": ["Salad", "Side dish"],
        "ingredients": ["cabbage", "carrots", "mayonnaise", "vinegar", "sugar", "salt"],
        "time": 10,
        "servings": 6,
        "instructions": "Creamy cabbage salad."
    },
    
    # More Indian Recipes
    {
        "id": "fallback_061",
        "title": "Aloo Gobi (Potato Cauliflower)",
        "cuisine": "Indian",
        "category": ["Vegetarian", "Vegan"],
        "ingredients": ["potatoes", "cauliflower", "tomatoes", "onion", "spices", "oil"],
        "time": 30,
        "servings": 4,
        "instructions": "Spiced potato and cauliflower curry."
    },
    {
        "id": "fallback_062",
        "title": "Butter Chicken",
        "cuisine": "Indian",
        "category": ["Curry", "Popular"],
        "ingredients": ["chicken", "butter", "cream", "tomato", "onion", "garlic", "spices"],
        "time": 45,
        "servings": 4,
        "instructions": "Rich and creamy tomato chicken curry."
    },
    {
        "id": "fallback_063",
        "title": "Samosas",
        "cuisine": "Indian",
        "category": ["Appetizer", "Fried"],
        "ingredients": ["potatoes", "peas", "flour", "spices", "oil", "onion"],
        "time": 45,
        "servings": 8,
        "instructions": "Crispy fried pastries with spiced filling."
    },
    
    # More Italian Recipes
    {
        "id": "fallback_064",
        "title": "Risotto",
        "cuisine": "Italian",
        "category": ["Rice", "Creamy"],
        "ingredients": ["arborio rice", "parmesan", "butter", "white wine", "broth", "onion"],
        "time": 35,
        "servings": 4,
        "instructions": "Creamy Italian rice dish."
    },
    {
        "id": "fallback_065",
        "title": "Caprese Salad",
        "cuisine": "Italian",
        "category": ["Salad", "Simple"],
        "ingredients": ["tomatoes", "mozzarella", "basil", "olive oil", "balsamic vinegar", "salt"],
        "time": 5,
        "servings": 4,
        "instructions": "Simple tomato and mozzarella salad."
    },
    {
        "id": "fallback_066",
        "title": "Minestrone Soup",
        "cuisine": "Italian",
        "category": ["Soup", "Vegetarian"],
        "ingredients": ["mixed vegetables", "pasta", "beans", "tomatoes", "broth", "garlic"],
        "time": 40,
        "servings": 6,
        "instructions": "Italian vegetable soup."
    },
    
    # More Mexican Recipes
    {
        "id": "fallback_067",
        "title": "Nachos",
        "cuisine": "Mexican",
        "category": ["Appetizer", "Cheese"],
        "ingredients": ["tortilla chips", "cheese", "beans", "jalapeños", "sour cream", "salsa"],
        "time": 15,
        "servings": 4,
        "instructions": "Loaded cheese nachos."
    },
    {
        "id": "fallback_068",
        "title": "Fajitas",
        "cuisine": "Mexican",
        "category": ["Grilled", "Quick"],
        "ingredients": ["chicken", "bell peppers", "onion", "tortillas", "lime", "spices"],
        "time": 25,
        "servings": 4,
        "instructions": "Sizzling chicken and pepper wraps."
    },
    {
        "id": "fallback_069",
        "title": "Chili Con Carne",
        "cuisine": "Mexican-American",
        "category": ["Stew", "Hearty"],
        "ingredients": ["ground beef", "beans", "tomatoes", "onion", "chili powder", "garlic"],
        "time": 60,
        "servings": 6,
        "instructions": "Spicy meat and bean stew."
    },
    
    # More Quick & Easy
    {
        "id": "fallback_070",
        "title": "Avocado Toast",
        "cuisine": "Universal",
        "category": ["Breakfast", "Quick", "Healthy"],
        "ingredients": ["avocado", "bread", "lemon", "salt", "pepper", "olive oil"],
        "time": 5,
        "servings": 1,
        "instructions": "Simple smashed avocado on toast."
    },
    
    # Seafood Recipes
    {
        "id": "fallback_071",
        "title": "Grilled Salmon",
        "cuisine": "Universal",
        "category": ["Seafood", "Healthy", "Quick"],
        "ingredients": ["salmon", "lemon", "garlic", "olive oil", "salt", "pepper", "dill"],
        "time": 20,
        "servings": 4,
        "instructions": "Simple grilled salmon with lemon and herbs."
    },
    {
        "id": "fallback_072",
        "title": "Fish Tacos",
        "cuisine": "Mexican",
        "category": ["Seafood", "Quick"],
        "ingredients": ["white fish", "tortillas", "cabbage", "lime", "sour cream", "spices"],
        "time": 25,
        "servings": 4,
        "instructions": "Crispy fish tacos with slaw."
    },
    {
        "id": "fallback_073",
        "title": "Shrimp Stir Fry",
        "cuisine": "Asian",
        "category": ["Seafood", "Quick", "Healthy"],
        "ingredients": ["shrimp", "vegetables", "soy sauce", "garlic", "ginger", "oil", "rice"],
        "time": 15,
        "servings": 4,
        "instructions": "Quick shrimp and vegetable stir fry."
    },
    {
        "id": "fallback_074",
        "title": "Tuna Salad",
        "cuisine": "Universal",
        "category": ["Seafood", "Quick", "Cold"],
        "ingredients": ["tuna", "mayonnaise", "celery", "onion", "lemon", "salt", "pepper"],
        "time": 10,
        "servings": 2,
        "instructions": "Classic tuna salad."
    },
    {
        "id": "fallback_075",
        "title": "Garlic Butter Shrimp",
        "cuisine": "Universal",
        "category": ["Seafood", "Quick"],
        "ingredients": ["shrimp", "butter", "garlic", "lemon", "parsley", "white wine"],
        "time": 15,
        "servings": 4,
        "instructions": "Pan-seared shrimp in garlic butter."
    },
    {
        "id": "fallback_076",
        "title": "Fish and Chips",
        "cuisine": "British",
        "category": ["Seafood", "Fried"],
        "ingredients": ["white fish", "potatoes", "flour", "beer", "oil", "salt", "vinegar"],
        "time": 40,
        "servings": 4,
        "instructions": "Classic British battered fish with fries."
    },
    {
        "id": "fallback_077",
        "title": "Shrimp Scampi",
        "cuisine": "Italian",
        "category": ["Seafood", "Pasta"],
        "ingredients": ["shrimp", "pasta", "garlic", "butter", "white wine", "lemon", "parsley"],
        "time": 25,
        "servings": 4,
        "instructions": "Garlic butter shrimp with linguine."
    },
    {
        "id": "fallback_078",
        "title": "Baked Cod",
        "cuisine": "Universal",
        "category": ["Seafood", "Healthy"],
        "ingredients": ["cod", "lemon", "butter", "breadcrumbs", "garlic", "herbs"],
        "time": 25,
        "servings": 4,
        "instructions": "Oven-baked cod with herb crust."
    },
    {
        "id": "fallback_079",
        "title": "Crab Cakes",
        "cuisine": "American",
        "category": ["Seafood", "Appetizer"],
        "ingredients": ["crab meat", "breadcrumbs", "egg", "mayonnaise", "mustard", "onion", "spices"],
        "time": 30,
        "servings": 4,
        "instructions": "Pan-fried crab cakes."
    },
    {
        "id": "fallback_080",
        "title": "Lobster Roll",
        "cuisine": "American",
        "category": ["Seafood", "Sandwich"],
        "ingredients": ["lobster", "mayonnaise", "celery", "lemon", "butter", "hot dog buns", "lettuce"],
        "time": 20,
        "servings": 4,
        "instructions": "Maine-style lobster roll."
    },
    
    # Vegetarian & Vegan Recipes
    {
        "id": "fallback_081",
        "title": "Vegetable Stir Fry",
        "cuisine": "Asian",
        "category": ["Vegetarian", "Vegan", "Quick"],
        "ingredients": ["mixed vegetables", "soy sauce", "garlic", "ginger", "oil", "rice"],
        "time": 15,
        "servings": 4,
        "instructions": "Quick mixed vegetable stir fry."
    },
    {
        "id": "fallback_082",
        "title": "Chickpea Curry",
        "cuisine": "Indian",
        "category": ["Vegetarian", "Vegan"],
        "ingredients": ["chickpeas", "tomatoes", "onion", "garlic", "curry powder", "coconut milk"],
        "time": 30,
        "servings": 4,
        "instructions": "Creamy chickpea curry."
    },
    {
        "id": "fallback_083",
        "title": "Veggie Burger",
        "cuisine": "American",
        "category": ["Vegetarian", "Quick"],
        "ingredients": ["black beans", "breadcrumbs", "egg", "onion", "spices", "burger buns", "lettuce"],
        "time": 25,
        "servings": 4,
        "instructions": "Homemade black bean burger."
    },
    {
        "id": "fallback_084",
        "title": "Ratatouille",
        "cuisine": "French",
        "category": ["Vegetarian", "Vegan"],
        "ingredients": ["eggplant", "zucchini", "tomatoes", "bell peppers", "onion", "garlic", "olive oil"],
        "time": 45,
        "servings": 6,
        "instructions": "French vegetable stew."
    },
    {
        "id": "fallback_085",
        "title": "Mushroom Risotto",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Creamy"],
        "ingredients": ["arborio rice", "mushrooms", "parmesan", "butter", "white wine", "broth", "onion"],
        "time": 35,
        "servings": 4,
        "instructions": "Creamy mushroom rice."
    },
    {
        "id": "fallback_086",
        "title": "Falafel",
        "cuisine": "Middle Eastern",
        "category": ["Vegetarian", "Vegan", "Fried"],
        "ingredients": ["chickpeas", "onion", "garlic", "parsley", "cumin", "coriander", "flour", "oil"],
        "time": 30,
        "servings": 4,
        "instructions": "Crispy fried chickpea balls."
    },
    {
        "id": "fallback_087",
        "title": "Spinach and Ricotta Stuffed Shells",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Pasta"],
        "ingredients": ["pasta shells", "ricotta", "spinach", "mozzarella", "tomato sauce", "garlic"],
        "time": 45,
        "servings": 6,
        "instructions": "Baked stuffed pasta shells."
    },
    {
        "id": "fallback_088",
        "title": "Vegetable Soup",
        "cuisine": "Universal",
        "category": ["Vegetarian", "Vegan", "Soup"],
        "ingredients": ["mixed vegetables", "vegetable broth", "tomatoes", "onion", "garlic", "herbs"],
        "time": 35,
        "servings": 6,
        "instructions": "Hearty vegetable soup."
    },
    {
        "id": "fallback_089",
        "title": "Tofu Scramble",
        "cuisine": "American",
        "category": ["Vegan", "Breakfast", "Quick"],
        "ingredients": ["tofu", "onion", "bell pepper", "turmeric", "nutritional yeast", "spices"],
        "time": 15,
        "servings": 2,
        "instructions": "Vegan scrambled eggs alternative."
    },
    {
        "id": "fallback_090",
        "title": "Lentil Soup",
        "cuisine": "Universal",
        "category": ["Vegetarian", "Vegan", "Soup"],
        "ingredients": ["lentils", "carrots", "celery", "onion", "garlic", "vegetable broth", "spices"],
        "time": 40,
        "servings": 6,
        "instructions": "Hearty lentil soup."
    },
    
    # Breakfast & Brunch
    {
        "id": "fallback_091",
        "title": "French Toast",
        "cuisine": "French",
        "category": ["Breakfast", "Quick"],
        "ingredients": ["bread", "eggs", "milk", "cinnamon", "vanilla", "butter", "syrup"],
        "time": 15,
        "servings": 4,
        "instructions": "Classic French toast."
    },
    {
        "id": "fallback_092",
        "title": "Pancakes",
        "cuisine": "American",
        "category": ["Breakfast", "Sweet"],
        "ingredients": ["flour", "eggs", "milk", "sugar", "baking powder", "butter", "syrup"],
        "time": 20,
        "servings": 4,
        "instructions": "Fluffy American pancakes."
    },
    {
        "id": "fallback_093",
        "title": "Eggs Benedict",
        "cuisine": "American",
        "category": ["Breakfast", "Brunch"],
        "ingredients": ["eggs", "english muffins", "ham", "butter", "lemon", "vinegar"],
        "time": 25,
        "servings": 2,
        "instructions": "Poached eggs with hollandaise."
    },
    {
        "id": "fallback_094",
        "title": "Breakfast Burrito",
        "cuisine": "Mexican-American",
        "category": ["Breakfast", "Quick"],
        "ingredients": ["eggs", "tortillas", "cheese", "beans", "salsa", "avocado"],
        "time": 15,
        "servings": 2,
        "instructions": "Hearty breakfast wrap."
    },
    {
        "id": "fallback_095",
        "title": "Omelette",
        "cuisine": "Universal",
        "category": ["Breakfast", "Quick"],
        "ingredients": ["eggs", "cheese", "vegetables", "butter", "salt", "pepper"],
        "time": 10,
        "servings": 1,
        "instructions": "Classic folded omelette."
    },
    {
        "id": "fallback_096",
        "title": "Smoothie Bowl",
        "cuisine": "Universal",
        "category": ["Breakfast", "Healthy", "Quick"],
        "ingredients": ["banana", "berries", "yogurt", "granola", "honey", "milk"],
        "time": 10,
        "servings": 1,
        "instructions": "Thick smoothie with toppings."
    },
    {
        "id": "fallback_097",
        "title": "Waffles",
        "cuisine": "Belgian",
        "category": ["Breakfast", "Sweet"],
        "ingredients": ["flour", "eggs", "milk", "sugar", "baking powder", "butter", "syrup"],
        "time": 20,
        "servings": 4,
        "instructions": "Crispy Belgian waffles."
    },
    {
        "id": "fallback_098",
        "title": "Breakfast Hash",
        "cuisine": "American",
        "category": ["Breakfast", "Hearty"],
        "ingredients": ["potatoes", "eggs", "onion", "bell pepper", "cheese", "salt", "pepper"],
        "time": 25,
        "servings": 4,
        "instructions": "Crispy potato and egg hash."
    },
    
    # Soups
    {
        "id": "fallback_099",
        "title": "Chicken Noodle Soup",
        "cuisine": "American",
        "category": ["Soup", "Comfort"],
        "ingredients": ["chicken", "noodles", "carrots", "celery", "onion", "chicken broth", "herbs"],
        "time": 45,
        "servings": 6,
        "instructions": "Classic chicken soup."
    },
    {
        "id": "fallback_100",
        "title": "Tomato Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Vegetarian"],
        "ingredients": ["tomatoes", "onion", "garlic", "cream", "vegetable broth", "basil"],
        "time": 30,
        "servings": 4,
        "instructions": "Creamy tomato soup."
    },
    {
        "id": "fallback_101",
        "title": "French Onion Soup",
        "cuisine": "French",
        "category": ["Soup", "Classic"],
        "ingredients": ["onions", "beef broth", "bread", "cheese", "butter", "white wine"],
        "time": 60,
        "servings": 4,
        "instructions": "Caramelized onion soup with cheese."
    },
    {
        "id": "fallback_102",
        "title": "Potato Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Comfort"],
        "ingredients": ["potatoes", "onion", "celery", "cream", "chicken broth", "bacon", "cheese"],
        "time": 35,
        "servings": 6,
        "instructions": "Creamy loaded potato soup."
    },
    {
        "id": "fallback_103",
        "title": "Miso Soup",
        "cuisine": "Japanese",
        "category": ["Soup", "Quick", "Light"],
        "ingredients": ["miso paste", "tofu", "seaweed", "green onion", "dashi", "water"],
        "time": 10,
        "servings": 4,
        "instructions": "Traditional Japanese miso soup."
    },
    {
        "id": "fallback_104",
        "title": "Butternut Squash Soup",
        "cuisine": "Universal",
        "category": ["Soup", "Vegetarian", "Healthy"],
        "ingredients": ["butternut squash", "onion", "garlic", "vegetable broth", "cream", "nutmeg"],
        "time": 45,
        "servings": 6,
        "instructions": "Creamy autumn soup."
    },
    {
        "id": "fallback_105",
        "title": "Beef Stew",
        "cuisine": "Universal",
        "category": ["Soup", "Stew", "Hearty"],
        "ingredients": ["beef", "potatoes", "carrots", "onion", "celery", "beef broth", "tomato paste"],
        "time": 120,
        "servings": 6,
        "instructions": "Slow-cooked beef stew."
    },
    {
        "id": "fallback_106",
        "title": "Clam Chowder",
        "cuisine": "American",
        "category": ["Soup", "Seafood"],
        "ingredients": ["clams", "potatoes", "onion", "celery", "cream", "bacon", "flour"],
        "time": 40,
        "servings": 6,
        "instructions": "Creamy New England clam chowder."
    },
    
    # Salads
    {
        "id": "fallback_107",
        "title": "Caesar Salad",
        "cuisine": "Italian-American",
        "category": ["Salad", "Classic"],
        "ingredients": ["romaine lettuce", "parmesan", "croutons", "caesar dressing", "lemon", "garlic"],
        "time": 10,
        "servings": 4,
        "instructions": "Classic Caesar salad."
    },
    {
        "id": "fallback_108",
        "title": "Greek Salad",
        "cuisine": "Greek",
        "category": ["Salad", "Healthy"],
        "ingredients": ["cucumber", "tomatoes", "feta", "olives", "red onion", "olive oil", "oregano"],
        "time": 10,
        "servings": 4,
        "instructions": "Traditional Greek salad."
    },
    {
        "id": "fallback_109",
        "title": "Cobb Salad",
        "cuisine": "American",
        "category": ["Salad", "Protein"],
        "ingredients": ["lettuce", "chicken", "bacon", "eggs", "avocado", "tomatoes", "blue cheese"],
        "time": 20,
        "servings": 4,
        "instructions": "Hearty American salad."
    },
    {
        "id": "fallback_110",
        "title": "Coleslaw",
        "cuisine": "American",
        "category": ["Salad", "Side"],
        "ingredients": ["cabbage", "carrots", "mayonnaise", "vinegar", "sugar", "salt", "pepper"],
        "time": 10,
        "servings": 6,
        "instructions": "Creamy cabbage salad."
    },
    {
        "id": "fallback_111",
        "title": "Potato Salad",
        "cuisine": "American",
        "category": ["Salad", "Side"],
        "ingredients": ["potatoes", "mayonnaise", "celery", "onion", "eggs", "mustard", "pickles"],
        "time": 30,
        "servings": 6,
        "instructions": "Classic potato salad."
    },
    {
        "id": "fallback_112",
        "title": "Caprese Pasta Salad",
        "cuisine": "Italian",
        "category": ["Salad", "Pasta"],
        "ingredients": ["pasta", "mozzarella", "tomatoes", "basil", "olive oil", "balsamic vinegar"],
        "time": 20,
        "servings": 6,
        "instructions": "Cold pasta salad."
    },
    {
        "id": "fallback_113",
        "title": "Asian Noodle Salad",
        "cuisine": "Asian",
        "category": ["Salad", "Noodles"],
        "ingredients": ["noodles", "vegetables", "soy sauce", "sesame oil", "peanuts", "ginger", "garlic"],
        "time": 20,
        "servings": 4,
        "instructions": "Cold Asian noodle salad."
    },
    {
        "id": "fallback_114",
        "title": "Quinoa Salad",
        "cuisine": "Universal",
        "category": ["Salad", "Healthy", "Vegetarian"],
        "ingredients": ["quinoa", "cucumber", "tomatoes", "feta", "lemon", "olive oil", "herbs"],
        "time": 25,
        "servings": 4,
        "instructions": "Nutritious grain salad."
    },
    
    # Beef Dishes
    {
        "id": "fallback_115",
        "title": "Beef Tacos",
        "cuisine": "Mexican",
        "category": ["Beef", "Quick"],
        "ingredients": ["ground beef", "taco shells", "lettuce", "tomatoes", "cheese", "salsa", "spices"],
        "time": 20,
        "servings": 4,
        "instructions": "Classic beef tacos."
    },
    {
        "id": "fallback_116",
        "title": "Beef Stroganoff",
        "cuisine": "Russian",
        "category": ["Beef", "Creamy"],
        "ingredients": ["beef", "mushrooms", "onion", "sour cream", "beef broth", "egg noodles"],
        "time": 35,
        "servings": 4,
        "instructions": "Creamy beef and mushroom dish."
    },
    {
        "id": "fallback_117",
        "title": "Steak Frites",
        "cuisine": "French",
        "category": ["Beef", "Classic"],
        "ingredients": ["steak", "potatoes", "butter", "garlic", "herbs", "oil", "salt"],
        "time": 30,
        "servings": 2,
        "instructions": "Grilled steak with fries."
    },
    {
        "id": "fallback_118",
        "title": "Beef and Broccoli",
        "cuisine": "Chinese-American",
        "category": ["Beef", "Quick"],
        "ingredients": ["beef", "broccoli", "soy sauce", "garlic", "ginger", "cornstarch", "rice"],
        "time": 25,
        "servings": 4,
        "instructions": "Stir-fried beef and broccoli."
    },
    {
        "id": "fallback_119",
        "title": "Meatloaf",
        "cuisine": "American",
        "category": ["Beef", "Comfort"],
        "ingredients": ["ground beef", "breadcrumbs", "eggs", "onion", "ketchup", "worcestershire sauce"],
        "time": 60,
        "servings": 6,
        "instructions": "Classic American meatloaf."
    },
    {
        "id": "fallback_120",
        "title": "Beef Enchiladas",
        "cuisine": "Mexican",
        "category": ["Beef", "Baked"],
        "ingredients": ["ground beef", "tortillas", "enchilada sauce", "cheese", "onion", "spices"],
        "time": 40,
        "servings": 6,
        "instructions": "Baked beef enchiladas."
    },
    
    # Pork Dishes
    {
        "id": "fallback_121",
        "title": "Pork Chops",
        "cuisine": "Universal",
        "category": ["Pork", "Quick"],
        "ingredients": ["pork chops", "garlic", "butter", "thyme", "salt", "pepper"],
        "time": 20,
        "servings": 4,
        "instructions": "Pan-seared pork chops."
    },
    {
        "id": "fallback_122",
        "title": "Pulled Pork",
        "cuisine": "American",
        "category": ["Pork", "BBQ"],
        "ingredients": ["pork shoulder", "bbq sauce", "onion", "spices", "burger buns", "coleslaw"],
        "time": 240,
        "servings": 8,
        "instructions": "Slow-cooked pulled pork."
    },
    {
        "id": "fallback_123",
        "title": "Sweet and Sour Pork",
        "cuisine": "Chinese",
        "category": ["Pork", "Sweet"],
        "ingredients": ["pork", "pineapple", "bell peppers", "vinegar", "sugar", "ketchup", "soy sauce"],
        "time": 30,
        "servings": 4,
        "instructions": "Chinese sweet and sour pork."
    },
    {
        "id": "fallback_124",
        "title": "Pork Stir Fry",
        "cuisine": "Asian",
        "category": ["Pork", "Quick"],
        "ingredients": ["pork", "vegetables", "soy sauce", "garlic", "ginger", "rice", "oil"],
        "time": 20,
        "servings": 4,
        "instructions": "Quick pork and vegetable stir fry."
    },
    {
        "id": "fallback_125",
        "title": "Bacon Wrapped Chicken",
        "cuisine": "American",
        "category": ["Pork", "Chicken"],
        "ingredients": ["chicken breast", "bacon", "cream cheese", "jalapeños", "spices"],
        "time": 35,
        "servings": 4,
        "instructions": "Bacon-wrapped stuffed chicken."
    },
    {
        "id": "fallback_126",
        "title": "Pork Carnitas",
        "cuisine": "Mexican",
        "category": ["Pork", "Slow-cooked"],
        "ingredients": ["pork shoulder", "orange", "lime", "spices", "tortillas", "cilantro"],
        "time": 180,
        "servings": 8,
        "instructions": "Mexican slow-cooked pork."
    },
    
    # Lamb Dishes
    {
        "id": "fallback_127",
        "title": "Lamb Curry",
        "cuisine": "Indian",
        "category": ["Lamb", "Curry"],
        "ingredients": ["lamb", "yogurt", "tomatoes", "onion", "garlic", "ginger", "curry spices"],
        "time": 60,
        "servings": 4,
        "instructions": "Slow-cooked lamb curry."
    },
    {
        "id": "fallback_128",
        "title": "Greek Lamb Chops",
        "cuisine": "Greek",
        "category": ["Lamb", "Grilled"],
        "ingredients": ["lamb chops", "lemon", "garlic", "oregano", "olive oil", "salt", "pepper"],
        "time": 25,
        "servings": 4,
        "instructions": "Grilled Mediterranean lamb chops."
    },
    {
        "id": "fallback_129",
        "title": "Shepherd's Pie",
        "cuisine": "British",
        "category": ["Lamb", "Comfort"],
        "ingredients": ["ground lamb", "potatoes", "carrots", "peas", "onion", "gravy", "cheese"],
        "time": 60,
        "servings": 6,
        "instructions": "Classic British shepherd's pie."
    },
    {
        "id": "fallback_130",
        "title": "Lamb Kebabs",
        "cuisine": "Middle Eastern",
        "category": ["Lamb", "Grilled"],
        "ingredients": ["lamb", "bell peppers", "onion", "yogurt", "spices", "lemon"],
        "time": 30,
        "servings": 4,
        "instructions": "Grilled lamb skewers."
    },
    
    # Quick Meals (<15 minutes)
    {
        "id": "fallback_131",
        "title": "Quesadilla",
        "cuisine": "Mexican",
        "category": ["Quick", "Cheese"],
        "ingredients": ["tortillas", "cheese", "beans", "salsa", "sour cream"],
        "time": 10,
        "servings": 2,
        "instructions": "Quick cheese quesadilla."
    },
    {
        "id": "fallback_132",
        "title": "Caprese Sandwich",
        "cuisine": "Italian",
        "category": ["Quick", "Sandwich"],
        "ingredients": ["bread", "mozzarella", "tomatoes", "basil", "balsamic vinegar", "olive oil"],
        "time": 5,
        "servings": 1,
        "instructions": "Fresh Italian sandwich."
    },
    {
        "id": "fallback_133",
        "title": "Peanut Butter and Banana Sandwich",
        "cuisine": "American",
        "category": ["Quick", "Breakfast", "Sweet"],
        "ingredients": ["bread", "peanut butter", "banana", "honey"],
        "time": 5,
        "servings": 1,
        "instructions": "Classic PB and banana sandwich."
    },
    {
        "id": "fallback_134",
        "title": "Instant Ramen Upgrade",
        "cuisine": "Asian",
        "category": ["Quick", "Budget"],
        "ingredients": ["instant ramen", "egg", "green onion", "soy sauce", "sesame oil"],
        "time": 10,
        "servings": 1,
        "instructions": "Elevated instant ramen."
    },
    {
        "id": "fallback_135",
        "title": "BLT Sandwich",
        "cuisine": "American",
        "category": ["Quick", "Sandwich"],
        "ingredients": ["bacon", "lettuce", "tomato", "bread", "mayonnaise"],
        "time": 15,
        "servings": 2,
        "instructions": "Classic bacon lettuce tomato sandwich."
    },
    {
        "id": "fallback_136",
        "title": "Egg Fried Rice",
        "cuisine": "Asian",
        "category": ["Quick", "Rice"],
        "ingredients": ["rice", "eggs", "soy sauce", "vegetables", "green onion", "oil"],
        "time": 15,
        "servings": 2,
        "instructions": "Quick fried rice with egg."
    },
    {
        "id": "fallback_137",
        "title": "Hummus Wrap",
        "cuisine": "Mediterranean",
        "category": ["Quick", "Vegetarian", "Healthy"],
        "ingredients": ["tortilla", "hummus", "cucumber", "tomatoes", "lettuce", "feta"],
        "time": 5,
        "servings": 1,
        "instructions": "Quick Mediterranean wrap."
    },
    {
        "id": "fallback_138",
        "title": "Tuna Melt",
        "cuisine": "American",
        "category": ["Quick", "Sandwich"],
        "ingredients": ["tuna", "bread", "cheese", "mayonnaise", "butter"],
        "time": 10,
        "servings": 2,
        "instructions": "Grilled tuna and cheese sandwich."
    },
    {
        "id": "fallback_139",
        "title": "Bagel with Cream Cheese and Lox",
        "cuisine": "Jewish-American",
        "category": ["Quick", "Breakfast"],
        "ingredients": ["bagel", "cream cheese", "smoked salmon", "capers", "red onion", "lemon"],
        "time": 5,
        "servings": 1,
        "instructions": "Classic New York bagel."
    },
    {
        "id": "fallback_140",
        "title": "Cheese and Crackers Plate",
        "cuisine": "Universal",
        "category": ["Quick", "Appetizer", "Simple"],
        "ingredients": ["cheese", "crackers", "grapes", "nuts", "honey"],
        "time": 5,
        "servings": 2,
        "instructions": "Simple cheese board."
    },
    
    # More Pasta Dishes (15)
    {
        "id": "fallback_141",
        "title": "Fettuccine Alfredo",
        "cuisine": "Italian",
        "category": ["Pasta", "Creamy"],
        "ingredients": ["fettuccine", "cream", "parmesan", "butter", "garlic", "pepper"],
        "time": 20,
        "servings": 4,
        "instructions": "Creamy parmesan pasta."
    },
    {
        "id": "fallback_142",
        "title": "Penne Arrabbiata",
        "cuisine": "Italian",
        "category": ["Pasta", "Spicy"],
        "ingredients": ["penne", "tomatoes", "garlic", "red chili flakes", "olive oil", "parsley"],
        "time": 25,
        "servings": 4,
        "instructions": "Spicy tomato pasta."
    },
    {
        "id": "fallback_143",
        "title": "Lasagna",
        "cuisine": "Italian",
        "category": ["Pasta", "Baked"],
        "ingredients": ["lasagna noodles", "ground beef", "ricotta", "mozzarella", "tomato sauce", "onion"],
        "time": 90,
        "servings": 8,
        "instructions": "Classic baked lasagna."
    },
    {
        "id": "fallback_144",
        "title": "Pasta Primavera",
        "cuisine": "Italian",
        "category": ["Pasta", "Vegetarian"],
        "ingredients": ["pasta", "mixed vegetables", "olive oil", "garlic", "parmesan", "herbs"],
        "time": 25,
        "servings": 4,
        "instructions": "Fresh vegetable pasta."
    },
    {
        "id": "fallback_145",
        "title": "Macaroni Salad",
        "cuisine": "American",
        "category": ["Pasta", "Salad", "Side"],
        "ingredients": ["macaroni", "mayonnaise", "celery", "onion", "carrots", "vinegar"],
        "time": 20,
        "servings": 6,
        "instructions": "Cold pasta salad."
    },
    {
        "id": "fallback_146",
        "title": "Baked Ziti",
        "cuisine": "Italian",
        "category": ["Pasta", "Baked"],
        "ingredients": ["ziti", "ricotta", "mozzarella", "tomato sauce", "parmesan", "basil"],
        "time": 45,
        "servings": 6,
        "instructions": "Baked cheesy pasta."
    },
    {
        "id": "fallback_147",
        "title": "Pesto Pasta",
        "cuisine": "Italian",
        "category": ["Pasta", "Quick"],
        "ingredients": ["pasta", "basil pesto", "parmesan", "pine nuts", "olive oil", "garlic"],
        "time": 15,
        "servings": 4,
        "instructions": "Simple basil pesto pasta."
    },
    {
        "id": "fallback_148",
        "title": "Pasta e Fagioli",
        "cuisine": "Italian",
        "category": ["Pasta", "Soup"],
        "ingredients": ["pasta", "white beans", "tomatoes", "onion", "garlic", "vegetable broth"],
        "time": 35,
        "servings": 6,
        "instructions": "Italian pasta and bean soup."
    },
    {
        "id": "fallback_149",
        "title": "Ravioli with Butter Sage Sauce",
        "cuisine": "Italian",
        "category": ["Pasta", "Quick"],
        "ingredients": ["ravioli", "butter", "sage", "parmesan", "garlic", "pepper"],
        "time": 15,
        "servings": 4,
        "instructions": "Simple butter sage ravioli."
    },
    {
        "id": "fallback_150",
        "title": "Pasta Carbonara",
        "cuisine": "Italian",
        "category": ["Pasta", "Creamy"],
        "ingredients": ["spaghetti", "bacon", "eggs", "parmesan", "black pepper", "garlic"],
        "time": 20,
        "servings": 4,
        "instructions": "Classic Roman pasta."
    },
    {
        "id": "fallback_151",
        "title": "Tortellini Soup",
        "cuisine": "Italian",
        "category": ["Pasta", "Soup"],
        "ingredients": ["tortellini", "chicken broth", "spinach", "tomatoes", "garlic", "parmesan"],
        "time": 25,
        "servings": 4,
        "instructions": "Cheesy tortellini soup."
    },
    {
        "id": "fallback_152",
        "title": "Linguine with Clam Sauce",
        "cuisine": "Italian",
        "category": ["Pasta", "Seafood"],
        "ingredients": ["linguine", "clams", "white wine", "garlic", "olive oil", "parsley"],
        "time": 30,
        "servings": 4,
        "instructions": "Seafood pasta with clams."
    },
    {
        "id": "fallback_153",
        "title": "Orzo Salad",
        "cuisine": "Mediterranean",
        "category": ["Pasta", "Salad"],
        "ingredients": ["orzo", "feta", "olives", "cucumber", "tomatoes", "lemon", "olive oil"],
        "time": 20,
        "servings": 4,
        "instructions": "Mediterranean pasta salad."
    },
    {
        "id": "fallback_154",
        "title": "Pasta Puttanesca",
        "cuisine": "Italian",
        "category": ["Pasta", "Quick"],
        "ingredients": ["spaghetti", "tomatoes", "olives", "capers", "anchovies", "garlic", "chili"],
        "time": 20,
        "servings": 4,
        "instructions": "Bold flavored pasta."
    },
    {
        "id": "fallback_155",
        "title": "Gnocchi with Tomato Sauce",
        "cuisine": "Italian",
        "category": ["Pasta", "Comfort"],
        "ingredients": ["gnocchi", "tomato sauce", "mozzarella", "basil", "garlic", "olive oil"],
        "time": 25,
        "servings": 4,
        "instructions": "Potato dumplings in sauce."
    },
    
    # More Asian Dishes (15)
    {
        "id": "fallback_156",
        "title": "Teriyaki Chicken",
        "cuisine": "Japanese",
        "category": ["Asian", "Grilled"],
        "ingredients": ["chicken", "soy sauce", "mirin", "sugar", "ginger", "garlic", "sesame seeds"],
        "time": 30,
        "servings": 4,
        "instructions": "Glazed teriyaki chicken."
    },
    {
        "id": "fallback_157",
        "title": "Bibimbap",
        "cuisine": "Korean",
        "category": ["Asian", "Rice Bowl"],
        "ingredients": ["rice", "beef", "vegetables", "egg", "gochujang", "sesame oil", "soy sauce"],
        "time": 35,
        "servings": 4,
        "instructions": "Korean mixed rice bowl."
    },
    {
        "id": "fallback_158",
        "title": "Spring Rolls",
        "cuisine": "Vietnamese",
        "category": ["Asian", "Appetizer", "Fresh"],
        "ingredients": ["rice paper", "shrimp", "lettuce", "vermicelli", "carrots", "mint", "peanut sauce"],
        "time": 25,
        "servings": 4,
        "instructions": "Fresh Vietnamese spring rolls."
    },
    {
        "id": "fallback_159",
        "title": "Ramen Bowl",
        "cuisine": "Japanese",
        "category": ["Asian", "Soup", "Noodles"],
        "ingredients": ["ramen noodles", "broth", "pork", "egg", "green onion", "seaweed", "bamboo shoots"],
        "time": 40,
        "servings": 2,
        "instructions": "Japanese ramen soup."
    },
    {
        "id": "fallback_160",
        "title": "General Tso's Chicken",
        "cuisine": "Chinese-American",
        "category": ["Asian", "Fried"],
        "ingredients": ["chicken", "soy sauce", "vinegar", "sugar", "garlic", "ginger", "chili peppers"],
        "time": 30,
        "servings": 4,
        "instructions": "Sweet and spicy chicken."
    },
    {
        "id": "fallback_161",
        "title": "Dumplings",
        "cuisine": "Chinese",
        "category": ["Asian", "Appetizer"],
        "ingredients": ["dumpling wrappers", "ground pork", "cabbage", "ginger", "soy sauce", "sesame oil"],
        "time": 45,
        "servings": 4,
        "instructions": "Steamed or fried dumplings."
    },
    {
        "id": "fallback_162",
        "title": "Orange Chicken",
        "cuisine": "Chinese-American",
        "category": ["Asian", "Fried"],
        "ingredients": ["chicken", "orange juice", "soy sauce", "sugar", "vinegar", "ginger", "garlic"],
        "time": 30,
        "servings": 4,
        "instructions": "Sweet citrus chicken."
    },
    {
        "id": "fallback_163",
        "title": "Kimchi Fried Rice",
        "cuisine": "Korean",
        "category": ["Asian", "Rice", "Quick"],
        "ingredients": ["rice", "kimchi", "egg", "soy sauce", "sesame oil", "green onion", "bacon"],
        "time": 15,
        "servings": 2,
        "instructions": "Spicy Korean fried rice."
    },
    {
        "id": "fallback_164",
        "title": "Sesame Noodles",
        "cuisine": "Chinese",
        "category": ["Asian", "Noodles", "Cold"],
        "ingredients": ["noodles", "sesame oil", "soy sauce", "peanut butter", "garlic", "vinegar", "cucumber"],
        "time": 20,
        "servings": 4,
        "instructions": "Cold sesame noodle salad."
    },
    {
        "id": "fallback_165",
        "title": "Katsu Curry",
        "cuisine": "Japanese",
        "category": ["Asian", "Curry"],
        "ingredients": ["chicken", "panko", "curry sauce", "rice", "potatoes", "carrots", "onion"],
        "time": 40,
        "servings": 4,
        "instructions": "Breaded chicken curry."
    },
    {
        "id": "fallback_166",
        "title": "Bánh Mì",
        "cuisine": "Vietnamese",
        "category": ["Asian", "Sandwich"],
        "ingredients": ["baguette", "pork", "pickled vegetables", "cilantro", "jalapeño", "mayonnaise"],
        "time": 25,
        "servings": 4,
        "instructions": "Vietnamese sandwich."
    },
    {
        "id": "fallback_167",
        "title": "Yakisoba",
        "cuisine": "Japanese",
        "category": ["Asian", "Noodles"],
        "ingredients": ["yakisoba noodles", "cabbage", "pork", "carrots", "soy sauce", "worcestershire sauce"],
        "time": 20,
        "servings": 4,
        "instructions": "Stir-fried Japanese noodles."
    },
    {
        "id": "fallback_168",
        "title": "Mongolian Beef",
        "cuisine": "Chinese-American",
        "category": ["Asian", "Beef"],
        "ingredients": ["beef", "soy sauce", "brown sugar", "ginger", "garlic", "green onions", "rice"],
        "time": 25,
        "servings": 4,
        "instructions": "Sweet and savory beef."
    },
    {
        "id": "fallback_169",
        "title": "Congee",
        "cuisine": "Chinese",
        "category": ["Asian", "Soup", "Rice"],
        "ingredients": ["rice", "chicken broth", "ginger", "green onion", "soy sauce", "chicken", "egg"],
        "time": 60,
        "servings": 4,
        "instructions": "Rice porridge."
    },
    {
        "id": "fallback_170",
        "title": "Pho",
        "cuisine": "Vietnamese",
        "category": ["Asian", "Soup", "Noodles"],
        "ingredients": ["rice noodles", "beef", "beef broth", "ginger", "star anise", "basil", "lime"],
        "time": 90,
        "servings": 4,
        "instructions": "Vietnamese noodle soup."
    },
    
    # Desserts (10)
    {
        "id": "fallback_171",
        "title": "Brownies",
        "cuisine": "American",
        "category": ["Dessert", "Baked"],
        "ingredients": ["chocolate", "butter", "sugar", "eggs", "flour", "cocoa powder", "vanilla"],
        "time": 35,
        "servings": 12,
        "instructions": "Fudgy chocolate brownies."
    },
    {
        "id": "fallback_172",
        "title": "Chocolate Chip Cookies",
        "cuisine": "American",
        "category": ["Dessert", "Baked"],
        "ingredients": ["flour", "butter", "sugar", "eggs", "chocolate chips", "vanilla", "baking soda"],
        "time": 25,
        "servings": 24,
        "instructions": "Classic chocolate chip cookies."
    },
    {
        "id": "fallback_173",
        "title": "Tiramisu",
        "cuisine": "Italian",
        "category": ["Dessert", "Cold"],
        "ingredients": ["ladyfingers", "mascarpone", "eggs", "coffee", "cocoa powder", "sugar", "marsala"],
        "time": 30,
        "servings": 8,
        "instructions": "Italian coffee dessert."
    },
    {
        "id": "fallback_174",
        "title": "Apple Pie",
        "cuisine": "American",
        "category": ["Dessert", "Baked"],
        "ingredients": ["apples", "pie crust", "sugar", "cinnamon", "butter", "flour", "lemon"],
        "time": 90,
        "servings": 8,
        "instructions": "Classic American apple pie."
    },
    {
        "id": "fallback_175",
        "title": "Cheesecake",
        "cuisine": "American",
        "category": ["Dessert", "Baked"],
        "ingredients": ["cream cheese", "sugar", "eggs", "graham crackers", "butter", "vanilla", "sour cream"],
        "time": 120,
        "servings": 12,
        "instructions": "Creamy New York cheesecake."
    },
    {
        "id": "fallback_176",
        "title": "Crème Brûlée",
        "cuisine": "French",
        "category": ["Dessert", "Elegant"],
        "ingredients": ["cream", "egg yolks", "sugar", "vanilla", "salt"],
        "time": 60,
        "servings": 4,
        "instructions": "French custard with caramelized top."
    },
    {
        "id": "fallback_177",
        "title": "Chocolate Mousse",
        "cuisine": "French",
        "category": ["Dessert", "Cold"],
        "ingredients": ["dark chocolate", "cream", "eggs", "sugar", "vanilla"],
        "time": 20,
        "servings": 4,
        "instructions": "Light chocolate mousse."
    },
    {
        "id": "fallback_178",
        "title": "Banana Bread",
        "cuisine": "American",
        "category": ["Dessert", "Baked", "Breakfast"],
        "ingredients": ["bananas", "flour", "sugar", "eggs", "butter", "baking soda", "vanilla"],
        "time": 60,
        "servings": 10,
        "instructions": "Moist banana bread."
    },
    {
        "id": "fallback_179",
        "title": "Ice Cream Sundae",
        "cuisine": "American",
        "category": ["Dessert", "Cold", "Quick"],
        "ingredients": ["ice cream", "chocolate sauce", "whipped cream", "cherries", "nuts", "sprinkles"],
        "time": 5,
        "servings": 1,
        "instructions": "Classic ice cream sundae."
    },
    {
        "id": "fallback_180",
        "title": "Pavlova",
        "cuisine": "Australian",
        "category": ["Dessert", "Elegant"],
        "ingredients": ["egg whites", "sugar", "cornstarch", "vinegar", "cream", "berries"],
        "time": 90,
        "servings": 8,
        "instructions": "Meringue dessert with fruit."
    },
    
    # Snacks & Appetizers (10)
    {
        "id": "fallback_181",
        "title": "Buffalo Wings",
        "cuisine": "American",
        "category": ["Appetizer", "Fried"],
        "ingredients": ["chicken wings", "hot sauce", "butter", "garlic powder", "celery", "blue cheese"],
        "time": 35,
        "servings": 4,
        "instructions": "Spicy buffalo chicken wings."
    },
    {
        "id": "fallback_182",
        "title": "Mozzarella Sticks",
        "cuisine": "American",
        "category": ["Appetizer", "Fried"],
        "ingredients": ["mozzarella", "flour", "eggs", "breadcrumbs", "marinara sauce", "oil"],
        "time": 20,
        "servings": 4,
        "instructions": "Fried cheese sticks."
    },
    {
        "id": "fallback_183",
        "title": "Deviled Eggs",
        "cuisine": "American",
        "category": ["Appetizer", "Cold"],
        "ingredients": ["eggs", "mayonnaise", "mustard", "paprika", "salt", "pepper"],
        "time": 20,
        "servings": 6,
        "instructions": "Classic deviled eggs."
    },
    {
        "id": "fallback_184",
        "title": "Bruschetta",
        "cuisine": "Italian",
        "category": ["Appetizer", "Fresh"],
        "ingredients": ["baguette", "tomatoes", "basil", "garlic", "olive oil", "balsamic vinegar", "salt"],
        "time": 15,
        "servings": 6,
        "instructions": "Italian tomato toast."
    },
    {
        "id": "fallback_185",
        "title": "Spinach Artichoke Dip",
        "cuisine": "American",
        "category": ["Appetizer", "Dip"],
        "ingredients": ["spinach", "artichokes", "cream cheese", "sour cream", "parmesan", "garlic"],
        "time": 25,
        "servings": 8,
        "instructions": "Creamy baked dip."
    },
    {
        "id": "fallback_186",
        "title": "Stuffed Mushrooms",
        "cuisine": "Universal",
        "category": ["Appetizer", "Baked"],
        "ingredients": ["mushrooms", "cream cheese", "parmesan", "garlic", "breadcrumbs", "herbs"],
        "time": 30,
        "servings": 6,
        "instructions": "Baked stuffed mushroom caps."
    },
    {
        "id": "fallback_187",
        "title": "Chips and Salsa",
        "cuisine": "Mexican",
        "category": ["Snack", "Quick"],
        "ingredients": ["tortilla chips", "tomatoes", "onion", "jalapeño", "cilantro", "lime", "salt"],
        "time": 10,
        "servings": 4,
        "instructions": "Fresh salsa with chips."
    },
    {
        "id": "fallback_188",
        "title": "Popcorn",
        "cuisine": "Universal",
        "category": ["Snack", "Quick"],
        "ingredients": ["popcorn kernels", "butter", "salt"],
        "time": 5,
        "servings": 2,
        "instructions": "Buttered popcorn."
    },
    {
        "id": "fallback_189",
        "title": "Jalapeño Poppers",
        "cuisine": "American",
        "category": ["Appetizer", "Spicy"],
        "ingredients": ["jalapeños", "cream cheese", "cheddar", "bacon", "breadcrumbs"],
        "time": 30,
        "servings": 6,
        "instructions": "Stuffed jalapeño peppers."
    },
    {
        "id": "fallback_190",
        "title": "Cheese Fondue",
        "cuisine": "Swiss",
        "category": ["Appetizer", "Cheese"],
        "ingredients": ["gruyere", "white wine", "garlic", "cornstarch", "bread cubes", "lemon"],
        "time": 20,
        "servings": 4,
        "instructions": "Melted cheese dip."
    },
    
    # Side Dishes (10)
    {
        "id": "fallback_191",
        "title": "Garlic Bread",
        "cuisine": "Italian-American",
        "category": ["Side", "Bread"],
        "ingredients": ["baguette", "butter", "garlic", "parsley", "parmesan"],
        "time": 15,
        "servings": 6,
        "instructions": "Buttery garlic bread."
    },
    {
        "id": "fallback_192",
        "title": "Mashed Potatoes",
        "cuisine": "Universal",
        "category": ["Side", "Comfort"],
        "ingredients": ["potatoes", "butter", "milk", "salt", "pepper", "garlic"],
        "time": 30,
        "servings": 6,
        "instructions": "Creamy mashed potatoes."
    },
    {
        "id": "fallback_193",
        "title": "French Fries",
        "cuisine": "Universal",
        "category": ["Side", "Fried"],
        "ingredients": ["potatoes", "oil", "salt"],
        "time": 30,
        "servings": 4,
        "instructions": "Crispy french fries."
    },
    {
        "id": "fallback_194",
        "title": "Roasted Vegetables",
        "cuisine": "Universal",
        "category": ["Side", "Healthy"],
        "ingredients": ["mixed vegetables", "olive oil", "garlic", "herbs", "salt", "pepper"],
        "time": 35,
        "servings": 4,
        "instructions": "Oven-roasted vegetables."
    },
    {
        "id": "fallback_195",
        "title": "Corn on the Cob",
        "cuisine": "American",
        "category": ["Side", "Simple"],
        "ingredients": ["corn", "butter", "salt", "pepper"],
        "time": 15,
        "servings": 4,
        "instructions": "Boiled or grilled corn."
    },
    {
        "id": "fallback_196",
        "title": "Baked Beans",
        "cuisine": "American",
        "category": ["Side", "Comfort"],
        "ingredients": ["beans", "bacon", "onion", "brown sugar", "ketchup", "mustard"],
        "time": 60,
        "servings": 8,
        "instructions": "Sweet baked beans."
    },
    {
        "id": "fallback_197",
        "title": "Onion Rings",
        "cuisine": "American",
        "category": ["Side", "Fried"],
        "ingredients": ["onions", "flour", "eggs", "breadcrumbs", "oil", "salt"],
        "time": 25,
        "servings": 4,
        "instructions": "Crispy fried onion rings."
    },
    {
        "id": "fallback_198",
        "title": "Steamed Broccoli",
        "cuisine": "Universal",
        "category": ["Side", "Healthy", "Quick"],
        "ingredients": ["broccoli", "butter", "lemon", "garlic", "salt"],
        "time": 10,
        "servings": 4,
        "instructions": "Simple steamed broccoli."
    },
    {
        "id": "fallback_199",
        "title": "Rice Pilaf",
        "cuisine": "Middle Eastern",
        "category": ["Side", "Rice"],
        "ingredients": ["rice", "butter", "onion", "broth", "herbs", "nuts"],
        "time": 25,
        "servings": 6,
        "instructions": "Seasoned rice pilaf."
    },
    {
        "id": "fallback_200",
        "title": "Sweet Potato Fries",
        "cuisine": "American",
        "category": ["Side", "Healthy"],
        "ingredients": ["sweet potatoes", "olive oil", "paprika", "salt", "pepper"],
        "time": 30,
        "servings": 4,
        "instructions": "Baked sweet potato fries."
    },
    
    # More Chicken Dishes (10)
    {
        "id": "fallback_201",
        "title": "Chicken Parmesan",
        "cuisine": "Italian-American",
        "category": ["Chicken", "Baked"],
        "ingredients": ["chicken breast", "marinara sauce", "mozzarella", "parmesan", "breadcrumbs", "pasta"],
        "time": 40,
        "servings": 4,
        "instructions": "Breaded chicken with cheese."
    },
    {
        "id": "fallback_202",
        "title": "Chicken Marsala",
        "cuisine": "Italian",
        "category": ["Chicken", "Elegant"],
        "ingredients": ["chicken breast", "mushrooms", "marsala wine", "butter", "garlic", "flour"],
        "time": 30,
        "servings": 4,
        "instructions": "Chicken in mushroom wine sauce."
    },
    {
        "id": "fallback_203",
        "title": "Lemon Chicken",
        "cuisine": "Universal",
        "category": ["Chicken", "Quick"],
        "ingredients": ["chicken", "lemon", "garlic", "butter", "herbs", "white wine"],
        "time": 25,
        "servings": 4,
        "instructions": "Bright lemon chicken."
    },
    {
        "id": "fallback_204",
        "title": "Chicken Enchiladas",
        "cuisine": "Mexican",
        "category": ["Chicken", "Baked"],
        "ingredients": ["chicken", "tortillas", "enchilada sauce", "cheese", "onion", "sour cream"],
        "time": 40,
        "servings": 6,
        "instructions": "Baked chicken enchiladas."
    },
    {
        "id": "fallback_205",
        "title": "Chicken Pot Pie",
        "cuisine": "American",
        "category": ["Chicken", "Comfort"],
        "ingredients": ["chicken", "mixed vegetables", "cream", "pie crust", "butter", "flour"],
        "time": 60,
        "servings": 6,
        "instructions": "Creamy chicken pot pie."
    },
    {
        "id": "fallback_206",
        "title": "BBQ Chicken",
        "cuisine": "American",
        "category": ["Chicken", "Grilled"],
        "ingredients": ["chicken", "bbq sauce", "onion", "spices", "butter"],
        "time": 35,
        "servings": 4,
        "instructions": "Grilled BBQ chicken."
    },
    {
        "id": "fallback_207",
        "title": "Chicken Shawarma",
        "cuisine": "Middle Eastern",
        "category": ["Chicken", "Grilled"],
        "ingredients": ["chicken", "yogurt", "lemon", "garlic", "spices", "pita bread", "tahini"],
        "time": 35,
        "servings": 4,
        "instructions": "Middle Eastern spiced chicken."
    },
    {
        "id": "fallback_208",
        "title": "Chicken Cacciatore",
        "cuisine": "Italian",
        "category": ["Chicken", "Stew"],
        "ingredients": ["chicken", "tomatoes", "bell peppers", "onion", "mushrooms", "wine", "herbs"],
        "time": 50,
        "servings": 4,
        "instructions": "Italian hunter's chicken."
    },
    {
        "id": "fallback_209",
        "title": "Nashville Hot Chicken",
        "cuisine": "American",
        "category": ["Chicken", "Fried", "Spicy"],
        "ingredients": ["chicken", "flour", "cayenne pepper", "paprika", "buttermilk", "oil", "pickles"],
        "time": 45,
        "servings": 4,
        "instructions": "Spicy fried chicken."
    },
    {
        "id": "fallback_210",
        "title": "Chicken Satay",
        "cuisine": "Thai",
        "category": ["Chicken", "Grilled"],
        "ingredients": ["chicken", "peanut butter", "coconut milk", "soy sauce", "lime", "spices"],
        "time": 30,
        "servings": 4,
        "instructions": "Thai peanut chicken skewers."
    },
    
    # More Vegetarian (10)
    {
        "id": "fallback_211",
        "title": "Eggplant Parmesan",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Baked"],
        "ingredients": ["eggplant", "marinara sauce", "mozzarella", "parmesan", "breadcrumbs", "basil"],
        "time": 50,
        "servings": 6,
        "instructions": "Breaded eggplant with cheese."
    },
    {
        "id": "fallback_212",
        "title": "Stuffed Bell Peppers",
        "cuisine": "Universal",
        "category": ["Vegetarian", "Baked"],
        "ingredients": ["bell peppers", "rice", "tomatoes", "onion", "cheese", "herbs"],
        "time": 50,
        "servings": 4,
        "instructions": "Rice-stuffed peppers."
    },
    {
        "id": "fallback_213",
        "title": "Vegetable Curry",
        "cuisine": "Indian",
        "category": ["Vegetarian", "Vegan"],
        "ingredients": ["mixed vegetables", "coconut milk", "curry powder", "onion", "garlic", "ginger"],
        "time": 35,
        "servings": 4,
        "instructions": "Creamy vegetable curry."
    },
    {
        "id": "fallback_214",
        "title": "Black Bean Tacos",
        "cuisine": "Mexican",
        "category": ["Vegetarian", "Quick"],
        "ingredients": ["black beans", "taco shells", "lettuce", "tomatoes", "cheese", "salsa", "avocado"],
        "time": 15,
        "servings": 4,
        "instructions": "Vegetarian bean tacos."
    },
    {
        "id": "fallback_215",
        "title": "Margherita Pizza",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Pizza"],
        "ingredients": ["pizza dough", "tomato sauce", "mozzarella", "basil", "olive oil", "garlic"],
        "time": 25,
        "servings": 4,
        "instructions": "Classic margherita pizza."
    },
    {
        "id": "fallback_216",
        "title": "Caprese Sandwich",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Sandwich"],
        "ingredients": ["ciabatta", "mozzarella", "tomatoes", "basil", "balsamic vinegar", "olive oil"],
        "time": 10,
        "servings": 2,
        "instructions": "Fresh mozzarella sandwich."
    },
    {
        "id": "fallback_217",
        "title": "Portobello Mushroom Burger",
        "cuisine": "American",
        "category": ["Vegetarian", "Grilled"],
        "ingredients": ["portobello mushrooms", "burger buns", "lettuce", "tomato", "cheese", "balsamic"],
        "time": 20,
        "servings": 4,
        "instructions": "Grilled mushroom burger."
    },
    {
        "id": "fallback_218",
        "title": "Vegetable Lasagna",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Baked"],
        "ingredients": ["lasagna noodles", "ricotta", "mozzarella", "spinach", "zucchini", "tomato sauce"],
        "time": 75,
        "servings": 8,
        "instructions": "Layered vegetable lasagna."
    },
    {
        "id": "fallback_219",
        "title": "Buddha Bowl",
        "cuisine": "Universal",
        "category": ["Vegetarian", "Healthy"],
        "ingredients": ["quinoa", "chickpeas", "avocado", "vegetables", "tahini", "lemon"],
        "time": 30,
        "servings": 2,
        "instructions": "Grain and veggie bowl."
    },
    {
        "id": "fallback_220",
        "title": "Grilled Vegetable Sandwich",
        "cuisine": "Universal",
        "category": ["Vegetarian", "Grilled"],
        "ingredients": ["zucchini", "eggplant", "bell peppers", "bread", "pesto", "mozzarella"],
        "time": 25,
        "servings": 2,
        "instructions": "Grilled veggie panini."
    },
    
    # International Specialties (10)
    {
        "id": "fallback_221",
        "title": "Paella",
        "cuisine": "Spanish",
        "category": ["Rice", "Seafood"],
        "ingredients": ["rice", "shrimp", "mussels", "chicken", "saffron", "bell peppers", "peas"],
        "time": 60,
        "servings": 6,
        "instructions": "Spanish saffron rice."
    },
    {
        "id": "fallback_222",
        "title": "Beef Wellington",
        "cuisine": "British",
        "category": ["Beef", "Elegant"],
        "ingredients": ["beef tenderloin", "puff pastry", "mushrooms", "pâté", "eggs", "mustard"],
        "time": 90,
        "servings": 4,
        "instructions": "Beef wrapped in pastry."
    },
    {
        "id": "fallback_223",
        "title": "Moussaka",
        "cuisine": "Greek",
        "category": ["Baked", "Comfort"],
        "ingredients": ["eggplant", "ground beef", "béchamel sauce", "tomatoes", "onion", "cinnamon"],
        "time": 90,
        "servings": 8,
        "instructions": "Greek layered casserole."
    },
    {
        "id": "fallback_224",
        "title": "Schnitzel",
        "cuisine": "German",
        "category": ["Pork", "Fried"],
        "ingredients": ["pork", "flour", "eggs", "breadcrumbs", "lemon", "oil"],
        "time": 25,
        "servings": 4,
        "instructions": "Breaded pork cutlet."
    },
    {
        "id": "fallback_225",
        "title": "Goulash",
        "cuisine": "Hungarian",
        "category": ["Beef", "Stew"],
        "ingredients": ["beef", "onion", "paprika", "tomatoes", "bell peppers", "potatoes", "broth"],
        "time": 120,
        "servings": 6,
        "instructions": "Hungarian beef stew."
    },
    {
        "id": "fallback_226",
        "title": "Chicken Tikka",
        "cuisine": "Indian",
        "category": ["Chicken", "Grilled"],
        "ingredients": ["chicken", "yogurt", "tikka masala spices", "lemon", "ginger", "garlic"],
        "time": 35,
        "servings": 4,
        "instructions": "Indian spiced chicken."
    },
    {
        "id": "fallback_227",
        "title": "Jambalaya",
        "cuisine": "Cajun",
        "category": ["Rice", "Spicy", "One-pot"],
        "ingredients": ["rice", "chicken", "sausage", "shrimp", "bell peppers", "celery", "onion", "spices"],
        "time": 50,
        "servings": 6,
        "instructions": "Louisiana rice dish."
    },
    {
        "id": "fallback_228",
        "title": "Pierogi",
        "cuisine": "Polish",
        "category": ["Dumplings", "Comfort"],
        "ingredients": ["dumpling dough", "potatoes", "cheese", "onion", "butter", "sour cream"],
        "time": 60,
        "servings": 6,
        "instructions": "Polish potato dumplings."
    },
    {
        "id": "fallback_229",
        "title": "Empanadas",
        "cuisine": "Latin American",
        "category": ["Appetizer", "Baked"],
        "ingredients": ["empanada dough", "ground beef", "onion", "olives", "hard boiled eggs", "spices"],
        "time": 45,
        "servings": 12,
        "instructions": "Savory filled pastries."
    },
    {
        "id": "fallback_230",
        "title": "Biryani",
        "cuisine": "Indian",
        "category": ["Rice", "Spicy"],
        "ingredients": ["basmati rice", "chicken", "yogurt", "onion", "spices", "saffron", "mint"],
        "time": 60,
        "servings": 6,
        "instructions": "Fragrant Indian rice."
    },
    
    # More Sandwiches & Wraps (5)
    {
        "id": "fallback_231",
        "title": "Club Sandwich",
        "cuisine": "American",
        "category": ["Sandwich", "Classic"],
        "ingredients": ["bread", "turkey", "bacon", "lettuce", "tomato", "mayonnaise", "cheese"],
        "time": 15,
        "servings": 2,
        "instructions": "Triple-decker sandwich."
    },
    {
        "id": "fallback_232",
        "title": "Reuben Sandwich",
        "cuisine": "American",
        "category": ["Sandwich", "Grilled"],
        "ingredients": ["rye bread", "corned beef", "sauerkraut", "swiss cheese", "thousand island dressing"],
        "time": 15,
        "servings": 2,
        "instructions": "Grilled deli sandwich."
    },
    {
        "id": "fallback_233",
        "title": "Chicken Caesar Wrap",
        "cuisine": "American",
        "category": ["Wrap", "Quick"],
        "ingredients": ["tortilla", "chicken", "romaine lettuce", "parmesan", "caesar dressing", "croutons"],
        "time": 10,
        "servings": 2,
        "instructions": "Caesar salad wrap."
    },
    {
        "id": "fallback_234",
        "title": "Philly Cheesesteak",
        "cuisine": "American",
        "category": ["Sandwich", "Hot"],
        "ingredients": ["beef", "hoagie roll", "cheese", "onions", "bell peppers", "oil"],
        "time": 20,
        "servings": 4,
        "instructions": "Philadelphia steak sandwich."
    },
    {
        "id": "fallback_235",
        "title": "Greek Wrap",
        "cuisine": "Greek",
        "category": ["Wrap", "Healthy"],
        "ingredients": ["pita", "chicken", "cucumber", "tomatoes", "feta", "tzatziki", "lettuce"],
        "time": 15,
        "servings": 2,
        "instructions": "Mediterranean wrap."
    },
    
    # One-Pot Meals (5)
    {
        "id": "fallback_236",
        "title": "Chicken and Rice",
        "cuisine": "Universal",
        "category": ["One-pot", "Comfort"],
        "ingredients": ["chicken", "rice", "chicken broth", "onion", "garlic", "vegetables", "herbs"],
        "time": 40,
        "servings": 4,
        "instructions": "One-pot chicken rice."
    },
    {
        "id": "fallback_237",
        "title": "Chili",
        "cuisine": "American",
        "category": ["One-pot", "Stew"],
        "ingredients": ["ground beef", "kidney beans", "tomatoes", "onion", "chili powder", "cumin", "garlic"],
        "time": 60,
        "servings": 6,
        "instructions": "Hearty beef chili."
    },
    {
        "id": "fallback_238",
        "title": "Shakshuka",
        "cuisine": "Middle Eastern",
        "category": ["One-pot", "Breakfast"],
        "ingredients": ["eggs", "tomatoes", "bell peppers", "onion", "garlic", "cumin", "paprika"],
        "time": 30,
        "servings": 4,
        "instructions": "Eggs poached in tomato sauce."
    },
    {
        "id": "fallback_239",
        "title": "Arroz con Pollo",
        "cuisine": "Latin American",
        "category": ["One-pot", "Rice"],
        "ingredients": ["chicken", "rice", "tomatoes", "bell peppers", "onion", "saffron", "peas"],
        "time": 50,
        "servings": 6,
        "instructions": "Latin chicken and rice."
    },
    {
        "id": "fallback_240",
        "title": "Hoppin' John",
        "cuisine": "Southern American",
        "category": ["One-pot", "Rice"],
        "ingredients": ["black-eyed peas", "rice", "bacon", "onion", "celery", "bell pepper", "spices"],
        "time": 45,
        "servings": 6,
        "instructions": "Southern rice and peas."
    },
    
    # Mutton Recipes (User Priority!)
    {
        "id": "fallback_241",
        "title": "Mutton Rogan Josh",
        "cuisine": "Kashmiri",
        "category": ["Mutton", "Curry", "Spicy"],
        "ingredients": ["mutton", "yogurt", "onion", "tomato", "ginger", "garlic", "kashmiri chili", "spices", "oil"],
        "time": 90,
        "servings": 4,
        "instructions": "Famous Kashmiri red curry with tender mutton pieces."
    },
    {
        "id": "fallback_242",
        "title": "Mutton Biryani",
        "cuisine": "Indian",
        "category": ["Mutton", "Rice", "One-pot", "Special"],
        "ingredients": ["mutton", "rice", "yogurt", "onion", "saffron", "spices", "ghee", "mint"],
        "time": 120,
        "servings": 6,
        "instructions": "Aromatic layered rice with spiced mutton."
    },
    {
        "id": "fallback_243",
        "title": "Mutton Korma",
        "cuisine": "Indian",
        "category": ["Mutton", "Curry", "Rich"],
        "ingredients": ["mutton", "cream", "yogurt", "cashews", "onion", "spices", "ghee"],
        "time": 75,
        "servings": 4,
        "instructions": "Creamy, rich mutton curry with nuts."
    },
    {
        "id": "fallback_244",
        "title": "Mutton Keema",
        "cuisine": "Indian",
        "category": ["Mutton", "Minced", "Quick"],
        "ingredients": ["minced mutton", "peas", "onion", "tomato", "ginger", "garlic", "spices"],
        "time": 40,
        "servings": 4,
        "instructions": "Spiced minced mutton with peas."
    },
    {
        "id": "fallback_245",
        "title": "Mutton Curry",
        "cuisine": "Indian",
        "category": ["Mutton", "Curry", "Traditional"],
        "ingredients": ["mutton", "onion", "tomato", "yogurt", "ginger", "garlic", "curry spices", "oil"],
        "time": 80,
        "servings": 4,
        "instructions": "Traditional Indian mutton curry."
    },
    {
        "id": "fallback_246",
        "title": "Mutton Karahi",
        "cuisine": "Pakistani",
        "category": ["Mutton", "Spicy", "Wok"],
        "ingredients": ["mutton", "tomato", "green chili", "ginger", "garlic", "coriander", "spices", "oil"],
        "time": 70,
        "servings": 4,
        "instructions": "Spicy Pakistani wok-cooked mutton."
    },
    {
        "id": "fallback_247",
        "title": "Mutton Nihari",
        "cuisine": "Pakistani",
        "category": ["Mutton", "Slow-cooked", "Traditional"],
        "ingredients": ["mutton", "flour", "ginger", "garlic", "nihari spices", "ghee", "onion"],
        "time": 180,
        "servings": 6,
        "instructions": "Slow-cooked overnight mutton stew."
    },
    {
        "id": "fallback_248",
        "title": "Mutton Haleem",
        "cuisine": "Pakistani",
        "category": ["Mutton", "Porridge", "Traditional"],
        "ingredients": ["mutton", "wheat", "lentils", "barley", "ginger", "garlic", "spices", "ghee"],
        "time": 240,
        "servings": 8,
        "instructions": "Rich slow-cooked mutton and grain porridge."
    },
    {
        "id": "fallback_249",
        "title": "Mutton Seekh Kebab",
        "cuisine": "Pakistani",
        "category": ["Mutton", "Grilled", "Appetizer"],
        "ingredients": ["minced mutton", "onion", "green chili", "coriander", "ginger", "garlic", "spices"],
        "time": 40,
        "servings": 4,
        "instructions": "Spiced minced mutton grilled on skewers."
    },
    {
        "id": "fallback_250",
        "title": "Mutton Pulao",
        "cuisine": "Pakistani",
        "category": ["Mutton", "Rice", "One-pot"],
        "ingredients": ["mutton", "rice", "yogurt", "onion", "whole spices", "ghee", "ginger"],
        "time": 90,
        "servings": 6,
        "instructions": "Fragrant rice cooked with mutton."
    },
    {
        "id": "fallback_251",
        "title": "Mutton Do Pyaza",
        "cuisine": "Indian",
        "category": ["Mutton", "Curry", "Onion-based"],
        "ingredients": ["mutton", "onion", "tomato", "yogurt", "ginger", "garlic", "spices"],
        "time": 85,
        "servings": 4,
        "instructions": "Mutton curry with double onions."
    },
    {
        "id": "fallback_252",
        "title": "Mutton Vindaloo",
        "cuisine": "Goan",
        "category": ["Mutton", "Spicy", "Tangy"],
        "ingredients": ["mutton", "vinegar", "red chili", "garlic", "ginger", "spices", "potato"],
        "time": 90,
        "servings": 4,
        "instructions": "Spicy and tangy Goan mutton curry."
    },
    {
        "id": "fallback_253",
        "title": "Irish Mutton Stew",
        "cuisine": "Irish",
        "category": ["Mutton", "Stew", "Comfort"],
        "ingredients": ["mutton", "potato", "carrot", "onion", "parsley", "thyme", "stock"],
        "time": 150,
        "servings": 6,
        "instructions": "Traditional Irish mutton and vegetable stew."
    },
    {
        "id": "fallback_254",
        "title": "Moroccan Mutton Tagine",
        "cuisine": "Moroccan",
        "category": ["Mutton", "Stew", "Spiced"],
        "ingredients": ["mutton", "apricot", "almond", "onion", "ginger", "cinnamon", "saffron", "honey"],
        "time": 120,
        "servings": 6,
        "instructions": "Slow-cooked mutton with dried fruits and spices."
    },
    {
        "id": "fallback_255",
        "title": "Mutton Roast",
        "cuisine": "British",
        "category": ["Mutton", "Roasted", "Traditional"],
        "ingredients": ["mutton leg", "rosemary", "garlic", "olive oil", "potato", "carrot", "onion"],
        "time": 180,
        "servings": 8,
        "instructions": "Classic roasted mutton with vegetables."
    },
    
    # Pakistani Cuisine
    {
        "id": "fallback_256",
        "title": "Chicken Karahi",
        "cuisine": "Pakistani",
        "category": ["Chicken", "Spicy", "Popular"],
        "ingredients": ["chicken", "tomato", "green chili", "ginger", "garlic", "coriander", "spices"],
        "time": 45,
        "servings": 4,
        "instructions": "Popular Pakistani wok-cooked chicken."
    },
    {
        "id": "fallback_257",
        "title": "Aloo Gosht",
        "cuisine": "Pakistani",
        "category": ["Beef", "Potato", "Curry"],
        "ingredients": ["beef", "potato", "onion", "tomato", "ginger", "garlic", "spices", "yogurt"],
        "time": 90,
        "servings": 6,
        "instructions": "Beef and potato curry."
    },
    {
        "id": "fallback_258",
        "title": "Paya",
        "cuisine": "Pakistani",
        "category": ["Trotters", "Stew", "Traditional"],
        "ingredients": ["goat trotters", "ginger", "garlic", "onion", "spices", "lemon"],
        "time": 300,
        "servings": 6,
        "instructions": "Slow-cooked trotters stew."
    },
    {
        "id": "fallback_259",
        "title": "Chapli Kebab",
        "cuisine": "Pakistani",
        "category": ["Beef", "Patty", "Fried"],
        "ingredients": ["minced beef", "tomato", "onion", "coriander", "pomegranate seeds", "spices", "flour"],
        "time": 30,
        "servings": 4,
        "instructions": "Spiced flat beef patties from Peshawar."
    },
    {
        "id": "fallback_260",
        "title": "Aloo Keema",
        "cuisine": "Pakistani",
        "category": ["Minced meat", "Potato", "Quick"],
        "ingredients": ["minced meat", "potato", "peas", "onion", "tomato", "ginger", "garlic", "spices"],
        "time": 40,
        "servings": 4,
        "instructions": "Minced meat with potatoes and peas."
    },
    {
        "id": "fallback_261",
        "title": "Sindhi Biryani",
        "cuisine": "Pakistani",
        "category": ["Rice", "Spicy", "Special"],
        "ingredients": ["meat", "rice", "potato", "yogurt", "tomato", "plum", "spices", "mint"],
        "time": 120,
        "servings": 6,
        "instructions": "Spicy Sindhi-style biryani with plums."
    },
    {
        "id": "fallback_262",
        "title": "Lahori Chargha",
        "cuisine": "Pakistani",
        "category": ["Chicken", "Fried", "Special"],
        "ingredients": ["whole chicken", "yogurt", "spices", "lemon", "ginger", "garlic", "oil"],
        "time": 90,
        "servings": 4,
        "instructions": "Lahore-style marinated fried chicken."
    },
    {
        "id": "fallback_263",
        "title": "Balochi Sajji",
        "cuisine": "Pakistani",
        "category": ["Lamb", "Roasted", "Traditional"],
        "ingredients": ["whole lamb", "salt", "ginger paste", "garlic paste", "lemon", "rice"],
        "time": 180,
        "servings": 8,
        "instructions": "Balochi-style roasted whole lamb."
    },
    {
        "id": "fallback_264",
        "title": "Chicken Tikka Masala Pakistani Style",
        "cuisine": "Pakistani",
        "category": ["Chicken", "Curry", "Creamy"],
        "ingredients": ["chicken tikka", "tomato", "cream", "butter", "ginger", "garlic", "spices"],
        "time": 50,
        "servings": 4,
        "instructions": "Grilled chicken in creamy tomato sauce."
    },
    {
        "id": "fallback_265",
        "title": "Halwa Puri Chana",
        "cuisine": "Pakistani",
        "category": ["Breakfast", "Traditional", "Vegetarian"],
        "ingredients": ["chickpeas", "semolina", "flour", "sugar", "spices", "oil"],
        "time": 60,
        "servings": 4,
        "instructions": "Traditional Pakistani breakfast platter."
    },
    
    # Beef Recipes
    {
        "id": "fallback_266",
        "title": "Beef Stroganoff",
        "cuisine": "Russian",
        "category": ["Beef", "Creamy", "Pasta"],
        "ingredients": ["beef strips", "mushroom", "onion", "sour cream", "butter", "flour", "stock"],
        "time": 40,
        "servings": 4,
        "instructions": "Creamy Russian beef and mushroom dish."
    },
    {
        "id": "fallback_267",
        "title": "Beef Wellington",
        "cuisine": "British",
        "category": ["Beef", "Special", "Baked"],
        "ingredients": ["beef tenderloin", "mushroom", "puff pastry", "pâté", "mustard", "egg"],
        "time": 90,
        "servings": 4,
        "instructions": "Beef fillet in mushroom duxelles and pastry."
    },
    {
        "id": "fallback_268",
        "title": "Beef Bourguignon",
        "cuisine": "French",
        "category": ["Beef", "Stew", "Wine"],
        "ingredients": ["beef chunks", "red wine", "bacon", "mushroom", "pearl onion", "carrot", "herbs"],
        "time": 180,
        "servings": 6,
        "instructions": "Classic French beef stew in red wine."
    },
    {
        "id": "fallback_269",
        "title": "Korean Beef Bulgogi",
        "cuisine": "Korean",
        "category": ["Beef", "Grilled", "Marinated"],
        "ingredients": ["beef slices", "soy sauce", "sugar", "sesame oil", "garlic", "ginger", "pear"],
        "time": 30,
        "servings": 4,
        "instructions": "Sweet marinated grilled beef."
    },
    {
        "id": "fallback_270",
        "title": "Mongolian Beef",
        "cuisine": "Chinese-American",
        "category": ["Beef", "Stir-fry", "Sweet"],
        "ingredients": ["beef strips", "soy sauce", "brown sugar", "ginger", "garlic", "green onion"],
        "time": 25,
        "servings": 4,
        "instructions": "Sweet and savory beef stir-fry."
    },
    {
        "id": "fallback_271",
        "title": "Beef Rendang",
        "cuisine": "Indonesian",
        "category": ["Beef", "Curry", "Spicy"],
        "ingredients": ["beef", "coconut milk", "lemongrass", "galangal", "chili", "spices", "kaffir lime"],
        "time": 180,
        "servings": 6,
        "instructions": "Rich Indonesian spiced beef curry."
    },
    {
        "id": "fallback_272",
        "title": "Classic Beef Stew",
        "cuisine": "American",
        "category": ["Beef", "Stew", "Comfort"],
        "ingredients": ["beef chunks", "potato", "carrot", "celery", "onion", "tomato paste", "stock"],
        "time": 150,
        "servings": 6,
        "instructions": "Hearty beef and vegetable stew."
    },
    {
        "id": "fallback_273",
        "title": "Pot Roast",
        "cuisine": "American",
        "category": ["Beef", "Roasted", "Comfort"],
        "ingredients": ["beef roast", "potato", "carrot", "onion", "stock", "herbs"],
        "time": 240,
        "servings": 8,
        "instructions": "Slow-roasted beef with vegetables."
    },
    {
        "id": "fallback_274",
        "title": "Beef Chili",
        "cuisine": "Tex-Mex",
        "category": ["Beef", "Spicy", "One-pot"],
        "ingredients": ["ground beef", "beans", "tomato", "chili powder", "onion", "bell pepper", "cumin"],
        "time": 60,
        "servings": 6,
        "instructions": "Spicy beef and bean chili."
    },
    {
        "id": "fallback_275",
        "title": "Braised Short Ribs",
        "cuisine": "American",
        "category": ["Beef", "Braised", "Special"],
        "ingredients": ["beef short ribs", "red wine", "onion", "carrot", "celery", "tomato paste", "stock"],
        "time": 210,
        "servings": 4,
        "instructions": "Tender wine-braised beef ribs."
    },
    
    # Pork Recipes
    {
        "id": "fallback_276",
        "title": "Pork Carnitas",
        "cuisine": "Mexican",
        "category": ["Pork", "Slow-cooked", "Tacos"],
        "ingredients": ["pork shoulder", "orange", "lime", "cumin", "oregano", "garlic", "bay leaf"],
        "time": 180,
        "servings": 8,
        "instructions": "Mexican slow-cooked pulled pork."
    },
    {
        "id": "fallback_277",
        "title": "Pork Schnitzel",
        "cuisine": "German",
        "category": ["Pork", "Breaded", "Fried"],
        "ingredients": ["pork cutlets", "flour", "egg", "breadcrumbs", "lemon", "oil"],
        "time": 30,
        "servings": 4,
        "instructions": "Crispy breaded pork cutlets."
    },
    {
        "id": "fallback_278",
        "title": "Pork Vindaloo",
        "cuisine": "Goan",
        "category": ["Pork", "Curry", "Spicy"],
        "ingredients": ["pork", "vinegar", "red chili", "garlic", "ginger", "spices", "potato"],
        "time": 90,
        "servings": 4,
        "instructions": "Spicy tangy Goan pork curry."
    },
    {
        "id": "fallback_279",
        "title": "Sweet and Sour Pork",
        "cuisine": "Chinese",
        "category": ["Pork", "Sweet", "Fried"],
        "ingredients": ["pork", "pineapple", "bell pepper", "vinegar", "sugar", "ketchup", "cornstarch"],
        "time": 35,
        "servings": 4,
        "instructions": "Classic Chinese sweet and sour pork."
    },
    {
        "id": "fallback_280",
        "title": "Pork Adobo",
        "cuisine": "Filipino",
        "category": ["Pork", "Braised", "Tangy"],
        "ingredients": ["pork belly", "soy sauce", "vinegar", "garlic", "bay leaf", "peppercorn"],
        "time": 60,
        "servings": 4,
        "instructions": "Filipino braised pork in vinegar and soy."
    },
    {
        "id": "fallback_281",
        "title": "Pulled Pork",
        "cuisine": "American BBQ",
        "category": ["Pork", "BBQ", "Slow-cooked"],
        "ingredients": ["pork shoulder", "bbq rub", "bbq sauce", "onion", "apple cider vinegar"],
        "time": 480,
        "servings": 10,
        "instructions": "Slow-cooked BBQ pulled pork."
    },
    {
        "id": "fallback_282",
        "title": "Pork Tenderloin Medallions",
        "cuisine": "American",
        "category": ["Pork", "Quick", "Elegant"],
        "ingredients": ["pork tenderloin", "garlic", "herbs", "butter", "white wine", "cream"],
        "time": 30,
        "servings": 4,
        "instructions": "Pan-seared pork with creamy sauce."
    },
    {
        "id": "fallback_283",
        "title": "Char Siu",
        "cuisine": "Chinese",
        "category": ["Pork", "BBQ", "Sweet"],
        "ingredients": ["pork shoulder", "honey", "soy sauce", "hoisin sauce", "five-spice", "red food color"],
        "time": 120,
        "servings": 6,
        "instructions": "Chinese BBQ pork with sweet glaze."
    },
    {
        "id": "fallback_284",
        "title": "Pork Chops with Apples",
        "cuisine": "American",
        "category": ["Pork", "Pan-fried", "Sweet"],
        "ingredients": ["pork chops", "apple", "onion", "cider", "thyme", "butter"],
        "time": 35,
        "servings": 4,
        "instructions": "Pan-fried pork chops with caramelized apples."
    },
    {
        "id": "fallback_285",
        "title": "Tonkatsu",
        "cuisine": "Japanese",
        "category": ["Pork", "Breaded", "Fried"],
        "ingredients": ["pork cutlet", "flour", "egg", "panko", "cabbage", "tonkatsu sauce"],
        "time": 30,
        "servings": 4,
        "instructions": "Japanese breaded deep-fried pork cutlet."
    },
    
    # Turkish Cuisine
    {
        "id": "fallback_286",
        "title": "Iskender Kebab",
        "cuisine": "Turkish",
        "category": ["Lamb", "Yogurt", "Special"],
        "ingredients": ["lamb doner", "pita bread", "tomato sauce", "yogurt", "butter", "tomato", "pepper"],
        "time": 45,
        "servings": 4,
        "instructions": "Sliced doner over bread with yogurt and tomato sauce."
    },
    {
        "id": "fallback_287",
        "title": "Adana Kebab",
        "cuisine": "Turkish",
        "category": ["Lamb", "Grilled", "Spicy"],
        "ingredients": ["minced lamb", "red pepper", "onion", "garlic", "cumin", "paprika", "parsley"],
        "time": 40,
        "servings": 4,
        "instructions": "Spicy minced lamb kebab on skewers."
    },
    {
        "id": "fallback_288",
        "title": "Turkish Köfte",
        "cuisine": "Turkish",
        "category": ["Meatballs", "Grilled", "Popular"],
        "ingredients": ["ground beef", "onion", "parsley", "cumin", "paprika", "bread crumbs"],
        "time": 30,
        "servings": 4,
        "instructions": "Turkish spiced meatballs."
    },
    {
        "id": "fallback_289",
        "title": "Menemen",
        "cuisine": "Turkish",
        "category": ["Eggs", "Breakfast", "Vegetarian"],
        "ingredients": ["eggs", "tomato", "green pepper", "onion", "olive oil", "spices"],
        "time": 20,
        "servings": 2,
        "instructions": "Turkish scrambled eggs with vegetables."
    },
    {
        "id": "fallback_290",
        "title": "İmam Bayıldı",
        "cuisine": "Turkish",
        "category": ["Eggplant", "Vegetarian", "Stuffed"],
        "ingredients": ["eggplant", "onion", "tomato", "garlic", "olive oil", "parsley", "sugar"],
        "time": 60,
        "servings": 4,
        "instructions": "Stuffed eggplant in olive oil."
    },
    {
        "id": "fallback_291",
        "title": "Turkish Pide",
        "cuisine": "Turkish",
        "category": ["Bread", "Topped", "Baked"],
        "ingredients": ["flour", "yeast", "ground meat", "cheese", "egg", "tomato", "pepper"],
        "time": 90,
        "servings": 4,
        "instructions": "Turkish flatbread pizza."
    },
    {
        "id": "fallback_292",
        "title": "Lahmacun",
        "cuisine": "Turkish",
        "category": ["Flatbread", "Meat", "Thin crust"],
        "ingredients": ["flour", "minced meat", "tomato", "onion", "parsley", "spices", "lemon"],
        "time": 60,
        "servings": 6,
        "instructions": "Thin Turkish meat pizza."
    },
    {
        "id": "fallback_293",
        "title": "Mantı",
        "cuisine": "Turkish",
        "category": ["Dumplings", "Yogurt", "Traditional"],
        "ingredients": ["flour", "minced meat", "onion", "yogurt", "garlic", "butter", "paprika"],
        "time": 120,
        "servings": 6,
        "instructions": "Turkish dumplings with yogurt sauce."
    },
    
    # African Cuisine
    {
        "id": "fallback_294",
        "title": "Jollof Rice",
        "cuisine": "West African",
        "category": ["Rice", "One-pot", "Popular"],
        "ingredients": ["rice", "tomato", "onion", "bell pepper", "spices", "chicken stock", "oil"],
        "time": 50,
        "servings": 6,
        "instructions": "Popular West African tomato rice."
    },
    {
        "id": "fallback_295",
        "title": "Doro Wat",
        "cuisine": "Ethiopian",
        "category": ["Chicken", "Stew", "Spicy"],
        "ingredients": ["chicken", "onion", "berbere spice", "ginger", "garlic", "butter", "egg"],
        "time": 90,
        "servings": 6,
        "instructions": "Ethiopian spicy chicken stew."
    },
    {
        "id": "fallback_296",
        "title": "Egusi Soup",
        "cuisine": "Nigerian",
        "category": ["Soup", "Melon seeds", "Traditional"],
        "ingredients": ["egusi seeds", "meat", "fish", "spinach", "tomato", "onion", "palm oil", "spices"],
        "time": 60,
        "servings": 6,
        "instructions": "Nigerian melon seed soup."
    },
    {
        "id": "fallback_297",
        "title": "Bobotie",
        "cuisine": "South African",
        "category": ["Minced meat", "Baked", "Sweet"],
        "ingredients": ["minced meat", "bread", "milk", "egg", "curry powder", "raisins", "chutney", "almond"],
        "time": 75,
        "servings": 6,
        "instructions": "South African spiced meat casserole."
    },
    {
        "id": "fallback_298",
        "title": "Peri-Peri Chicken",
        "cuisine": "Mozambican",
        "category": ["Chicken", "Grilled", "Spicy"],
        "ingredients": ["chicken", "peri-peri chili", "garlic", "lemon", "paprika", "olive oil"],
        "time": 60,
        "servings": 4,
        "instructions": "Spicy African grilled chicken."
    },
    {
        "id": "fallback_299",
        "title": "Bunny Chow",
        "cuisine": "South African",
        "category": ["Curry", "Bread bowl", "Street food"],
        "ingredients": ["bread loaf", "curry", "meat", "potato", "onion", "tomato", "spices"],
        "time": 50,
        "servings": 4,
        "instructions": "South African curry in a bread bowl."
    },
    {
        "id": "fallback_300",
        "title": "Moroccan Bastilla",
        "cuisine": "Moroccan",
        "category": ["Chicken", "Pastry", "Sweet-savory"],
        "ingredients": ["chicken", "phyllo dough", "almond", "egg", "cinnamon", "sugar", "onion", "saffron"],
        "time": 120,
        "servings": 8,
        "instructions": "Moroccan sweet and savory chicken pie."
    },
    
    # Gluten-Free Recipes
    {
        "id": "fallback_301",
        "title": "Grilled Lemon Herb Chicken",
        "cuisine": "Mediterranean",
        "category": ["Chicken", "Gluten-free", "Grilled"],
        "ingredients": ["chicken breast", "lemon", "olive oil", "garlic", "rosemary", "thyme"],
        "time": 30,
        "servings": 4,
        "instructions": "Marinated grilled chicken with herbs."
    },
    {
        "id": "fallback_302",
        "title": "Quinoa Buddha Bowl",
        "cuisine": "Modern",
        "category": ["Vegetarian", "Gluten-free", "Healthy"],
        "ingredients": ["quinoa", "chickpeas", "avocado", "kale", "tahini", "lemon"],
        "time": 25,
        "servings": 4,
        "instructions": "Nutritious quinoa bowl with vegetables."
    },
    {
        "id": "fallback_303",
        "title": "Baked Salmon with Asparagus",
        "cuisine": "American",
        "category": ["Seafood", "Gluten-free", "Healthy"],
        "ingredients": ["salmon fillet", "asparagus", "lemon", "garlic", "olive oil", "dill"],
        "time": 25,
        "servings": 4,
        "instructions": "Simple baked salmon and asparagus."
    },
    {
        "id": "fallback_304",
        "title": "Mexican Chicken Fajita Bowl",
        "cuisine": "Mexican",
        "category": ["Chicken", "Gluten-free", "Rice bowl"],
        "ingredients": ["chicken", "bell peppers", "onion", "rice", "lime", "cilantro", "spices"],
        "time": 30,
        "servings": 4,
        "instructions": "Fajita-style chicken over rice."
    },
    {
        "id": "fallback_305",
        "title": "Cauliflower Rice Stir Fry",
        "cuisine": "Asian",
        "category": ["Vegetarian", "Gluten-free", "Low-carb"],
        "ingredients": ["cauliflower", "eggs", "carrots", "peas", "soy sauce", "sesame oil"],
        "time": 20,
        "servings": 4,
        "instructions": "Healthy cauliflower rice stir-fry."
    },
    {
        "id": "fallback_306",
        "title": "Greek Chicken Souvlaki",
        "cuisine": "Greek",
        "category": ["Chicken", "Gluten-free", "Grilled"],
        "ingredients": ["chicken", "lemon", "olive oil", "oregano", "garlic", "onion"],
        "time": 35,
        "servings": 4,
        "instructions": "Marinated Greek chicken skewers."
    },
    {
        "id": "fallback_307",
        "title": "Thai Coconut Curry Soup",
        "cuisine": "Thai",
        "category": ["Soup", "Gluten-free", "Chicken"],
        "ingredients": ["chicken", "coconut milk", "curry paste", "lemongrass", "lime", "vegetables"],
        "time": 30,
        "servings": 6,
        "instructions": "Creamy Thai coconut curry soup."
    },
    {
        "id": "fallback_308",
        "title": "Zucchini Noodles with Pesto",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Gluten-free", "Low-carb"],
        "ingredients": ["zucchini", "basil", "pine nuts", "parmesan", "garlic", "olive oil"],
        "time": 15,
        "servings": 4,
        "instructions": "Fresh zucchini noodles with basil pesto."
    },
    {
        "id": "fallback_309",
        "title": "Shrimp Avocado Salad",
        "cuisine": "American",
        "category": ["Seafood", "Gluten-free", "Salad"],
        "ingredients": ["shrimp", "avocado", "lettuce", "tomato", "lime", "cilantro"],
        "time": 15,
        "servings": 4,
        "instructions": "Fresh shrimp and avocado salad."
    },
    {
        "id": "fallback_310",
        "title": "Stuffed Bell Peppers with Ground Beef",
        "cuisine": "American",
        "category": ["Beef", "Gluten-free", "Baked"],
        "ingredients": ["bell peppers", "ground beef", "rice", "tomato sauce", "onion", "cheese"],
        "time": 50,
        "servings": 4,
        "instructions": "Baked peppers stuffed with beef and rice."
    },
    {
        "id": "fallback_311",
        "title": "Vietnamese Pho (Rice Noodle Soup)",
        "cuisine": "Vietnamese",
        "category": ["Soup", "Gluten-free", "Beef"],
        "ingredients": ["rice noodles", "beef", "beef broth", "ginger", "star anise", "onion", "herbs"],
        "time": 90,
        "servings": 6,
        "instructions": "Traditional Vietnamese beef noodle soup."
    },
    {
        "id": "fallback_312",
        "title": "Sweet Potato Buddha Bowl",
        "cuisine": "Modern",
        "category": ["Vegetarian", "Gluten-free", "Healthy"],
        "ingredients": ["sweet potato", "chickpeas", "spinach", "tahini", "quinoa", "avocado"],
        "time": 35,
        "servings": 4,
        "instructions": "Roasted sweet potato and chickpea bowl."
    },
    {
        "id": "fallback_313",
        "title": "Lemon Garlic Shrimp with Rice",
        "cuisine": "Mediterranean",
        "category": ["Seafood", "Gluten-free", "Quick"],
        "ingredients": ["shrimp", "rice", "lemon", "garlic", "butter", "parsley"],
        "time": 20,
        "servings": 4,
        "instructions": "Quick garlic shrimp over rice."
    },
    {
        "id": "fallback_314",
        "title": "Mexican Street Corn Salad",
        "cuisine": "Mexican",
        "category": ["Vegetarian", "Gluten-free", "Salad"],
        "ingredients": ["corn", "lime", "cotija cheese", "cilantro", "mayo", "chili powder"],
        "time": 15,
        "servings": 6,
        "instructions": "Mexican-style corn salad."
    },
    {
        "id": "fallback_315",
        "title": "Teriyaki Chicken with Vegetables",
        "cuisine": "Japanese",
        "category": ["Chicken", "Gluten-free", "Stir-fry"],
        "ingredients": ["chicken", "broccoli", "carrots", "gluten-free soy sauce", "honey", "ginger"],
        "time": 25,
        "servings": 4,
        "instructions": "Sweet and savory teriyaki chicken."
    },
    {
        "id": "fallback_316",
        "title": "Indian Chicken Curry",
        "cuisine": "Indian",
        "category": ["Chicken", "Gluten-free", "Curry"],
        "ingredients": ["chicken", "coconut milk", "curry powder", "tomato", "onion", "garlic", "ginger"],
        "time": 40,
        "servings": 4,
        "instructions": "Rich Indian chicken curry."
    },
    {
        "id": "fallback_317",
        "title": "Caprese Salad",
        "cuisine": "Italian",
        "category": ["Vegetarian", "Gluten-free", "Salad"],
        "ingredients": ["tomato", "mozzarella", "basil", "olive oil", "balsamic vinegar"],
        "time": 10,
        "servings": 4,
        "instructions": "Classic Italian tomato mozzarella salad."
    },
    {
        "id": "fallback_318",
        "title": "Grilled Steak with Chimichurri",
        "cuisine": "Argentinian",
        "category": ["Beef", "Gluten-free", "Grilled"],
        "ingredients": ["steak", "parsley", "garlic", "olive oil", "vinegar", "oregano"],
        "time": 25,
        "servings": 4,
        "instructions": "Grilled steak with chimichurri sauce."
    },
    {
        "id": "fallback_319",
        "title": "Egg Fried Rice",
        "cuisine": "Chinese",
        "category": ["Vegetarian", "Gluten-free", "Rice"],
        "ingredients": ["rice", "eggs", "peas", "carrots", "soy sauce", "sesame oil"],
        "time": 15,
        "servings": 4,
        "instructions": "Simple egg fried rice."
    },
    {
        "id": "fallback_320",
        "title": "Greek Lemon Chicken Soup",
        "cuisine": "Greek",
        "category": ["Soup", "Gluten-free", "Chicken"],
        "ingredients": ["chicken", "rice", "lemon", "eggs", "chicken broth", "dill"],
        "time": 45,
        "servings": 6,
        "instructions": "Traditional Greek avgolemono soup."
    },
]


# Build ingredient index for O(1) lookups instead of O(n*m) searches
_ingredient_index = None

def _build_ingredient_index():
    """
    Build an inverted index mapping ingredients to recipe IDs.
    This speeds up searches from O(recipes * ingredients) to O(user_ingredients).
    """
    global _ingredient_index
    if _ingredient_index is not None:
        return _ingredient_index
    
    _ingredient_index = {}
    for recipe in FALLBACK_RECIPES:
        for ingredient in recipe["ingredients"]:
            normalized = ingredient.lower().strip()
            if normalized not in _ingredient_index:
                _ingredient_index[normalized] = []
            _ingredient_index[normalized].append(recipe["id"])
    
    return _ingredient_index


def search_fallback_recipes(user_ingredients: List[str], max_results: int = 10, diet: str = None, max_minutes: int = None, sort_by: str = "relevance") -> List[Recipe]:
    """
    Search fallback recipes based on user ingredients.
    Returns recipes that match at least one ingredient.
    Optimized with ingredient index for fast lookups.
    
    Args:
        user_ingredients: List of ingredients user has
        max_results: Maximum results to return
        diet: Dietary filter (vegetarian, vegan, etc.)
        max_minutes: Maximum cooking time in minutes
        sort_by: Sort method (relevance, match-desc, used-desc, missing-asc, time-asc)
    
    Returns:
        List of matching recipes
    """
    from core.normalize import ingredients_match, find_matching_ingredients
    
    # Build index on first call (cached for subsequent calls)
    _build_ingredient_index()
    
    # Normalize user ingredients
    user_ings_normalized = [ing.lower().strip() for ing in user_ingredients]
    
    # Use index to quickly find candidate recipes
    candidate_recipe_ids = set()
    for user_ing in user_ings_normalized:
        # Check for exact matches in index
        for indexed_ing, recipe_ids in _ingredient_index.items():
            if ingredients_match(user_ing, indexed_ing):
                candidate_recipe_ids.update(recipe_ids)
    
    # Build recipe objects only for candidates
    results = []
    recipes_by_id = {r["id"]: r for r in FALLBACK_RECIPES}
    
    for recipe_id in candidate_recipe_ids:
        recipe_data = recipes_by_id[recipe_id]
        recipe_ings = recipe_data["ingredients"]
        
        # Find used and missing ingredients
        used, missing = find_matching_ingredients(user_ingredients, recipe_ings)
        
        # Create ingredient items
        ingredient_items = [
            IngredientItem(name=ing) for ing in recipe_ings
        ]
        
        # Create recipe object
        recipe = Recipe(
            id=recipe_data["id"],
            provider=Provider.THEMEALDB,  # Use TheMealDB as provider
            title=recipe_data["title"],
            image_url=None,
            source_url=f"https://www.google.com/search?q={recipe_data['title'].replace(' ', '+')}+recipe",
            ingredients=ingredient_items,
            used_ingredients=used,
            missing_ingredients=missing,
            instructions=recipe_data["instructions"],
            servings=recipe_data.get("servings"),
            ready_in_minutes=recipe_data.get("time"),
            cuisine=recipe_data.get("cuisine"),
            category_or_diet=recipe_data.get("category", []),
            cost_per_serving_usd=None
        )
        
        results.append(recipe)
    
    # Apply diet filter
    if diet:
        diet_lower = diet.lower()
        filtered_results = []
        for recipe in results:
            categories = [c.lower() for c in recipe.category_or_diet] if recipe.category_or_diet else []
            if diet_lower in categories:
                filtered_results.append(recipe)
        results = filtered_results
    
    # Apply max time filter
    if max_minutes is not None:
        results = [r for r in results if r.ready_in_minutes and r.ready_in_minutes <= max_minutes]
    
    # Sort based on sort_by parameter
    if sort_by == "relevance" or sort_by == "match-desc":
        # Smart sort: match % → used count → cooking time
        def smart_sort_key(recipe: Recipe):
            match_pct = recipe.match_percentage
            used_count = len(recipe.used_ingredients)
            time = recipe.ready_in_minutes if recipe.ready_in_minutes is not None else 999999
            return (-match_pct, -used_count, time)
        results.sort(key=smart_sort_key)
    elif sort_by == "used-desc":
        results.sort(key=lambda r: (-len(r.used_ingredients), -r.match_percentage))
    elif sort_by == "missing-asc":
        results.sort(key=lambda r: (len(r.missing_ingredients), -r.match_percentage))
    elif sort_by == "time-asc":
        results.sort(key=lambda r: (r.ready_in_minutes if r.ready_in_minutes is not None else 999999, -r.match_percentage))
    
    return results[:max_results]

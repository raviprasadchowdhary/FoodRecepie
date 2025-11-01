# 🎉 Recipe Library Expansion Guide

## Current Library: 70 Recipes! 🌍

Your Recipe Finder now includes **70 diverse recipes** from **15+ cuisines** around the world!

## 📊 Cuisine Breakdown

| Cuisine | Recipe Count | Examples |
|---------|--------------|----------|
| 🇮🇳 Indian | 8 recipes | Dal, Egg Curry, Biryani, Paneer Tikka, Tikka Masala, Aloo Gobi, Butter Chicken, Samosas |
| 🇲🇽 Mexican | 8 recipes | Tacos, Quesadillas, Guacamole, Burritos, Enchiladas, Nachos, Fajitas, Chili |
| 🇺🇸 American | 9 recipes | Cheeseburger, Mac & Cheese, Grilled Cheese, BBQ Wings, BLT, Pot Pie, Meatloaf, Coleslaw |
| 🇮🇹 Italian | 7 recipes | Carbonara, Pizza, Aglio e Olio, Lasagna, Risotto, Caprese, Minestrone |
| 🇬🇧 British | 4 recipes | Beans on Toast, Fish & Chips, Shepherd's Pie, English Breakfast |
| 🇹🇭 Thai | 3 recipes | Pad Thai, Green Curry, Tom Yum Soup |
| 🇰🇷 Korean | 3 recipes | Kimchi Fried Rice, Bibimbap, Bulgogi |
| 🇻🇳 Vietnamese | 3 recipes | Pho, Banh Mi, Spring Rolls |
| 🇪🇸 Spanish | 3 recipes | Tortilla, Paella, Gazpacho |
| 🇬🇷 Greek | 4 recipes | Greek Salad, Moussaka, Tzatziki, Gyros |
| 🇨🇳 Chinese | 3 recipes | Fried Rice, Egg Drop Soup, Stir-Fry |
| 🇯🇵 Japanese | 2 recipes | Miso Soup, Teriyaki Chicken |
| 🇫🇷 French | 1 recipe | French Toast |
| 🌍 Middle Eastern | 2 recipes | Hummus, Falafel |
| 🌐 Universal | 10 recipes | Omelette, Salads, Soups, Sandwiches, Pancakes, Avocado Toast |

**Total: 70 Recipes!**

---

## ➕ How to Add More Recipes

Want to add your own recipes? It's super easy! Just edit `providers/fallback_recipes.py`:

### Step 1: Find the FALLBACK_RECIPES list

Open `providers/fallback_recipes.py` and scroll to the bottom of the list (before the closing `]`).

### Step 2: Add Your Recipe

Copy this template and add your recipe:

```python
    {
        "id": "fallback_071",  # Increment the number
        "title": "Your Recipe Name",
        "cuisine": "Cuisine Type",  # e.g., "Italian", "Indian", "Thai"
        "category": ["Category1", "Category2"],  # e.g., ["Quick", "Vegetarian"]
        "ingredients": ["ingredient1", "ingredient2", "ingredient3"],
        "time": 25,  # cooking time in minutes
        "servings": 4,  # number of servings
        "instructions": "Brief description or cooking instructions."
    },
```

### Step 3: Save and Test!

That's it! Your recipe is now searchable.

---

## 📝 Real Example

Let's add a **Turkish Kebab**:

```python
    {
        "id": "fallback_071",
        "title": "Turkish Kebab",
        "cuisine": "Turkish",
        "category": ["Grilled", "Protein-rich"],
        "ingredients": ["beef", "onion", "bell peppers", "cumin", "paprika", "olive oil"],
        "time": 30,
        "servings": 4,
        "instructions": "Marinated and grilled beef skewers with vegetables."
    },
```

---

## 🎯 Category Options

Use these categories to help users find recipes:

### By Speed
- `"Quick"` - Under 15 minutes
- `"One-pot"` - Single dish cooking
- `"One-pan"` - Single pan cooking

### By Diet
- `"Vegetarian"` - No meat
- `"Vegan"` - No animal products
- `"Gluten-free"` - No gluten
- `"Keto"` - Low carb

### By Type
- `"Breakfast"` - Morning meals
- `"Lunch"` - Midday meals
- `"Dinner"` - Evening meals
- `"Appetizer"` - Starters
- `"Dessert"` - Sweets
- `"Snack"` - Light bites

### By Style
- `"Comfort food"` - Hearty, satisfying
- `"Healthy"` - Nutritious
- `"Budget-friendly"` - Inexpensive
- `"Popular"` - Well-known
- `"Traditional"` - Classic recipes

### By Cooking Method
- `"Baked"` - Oven-cooked
- `"Fried"` - Deep/pan fried
- `"Grilled"` - Grilled/BBQ
- `"Soup"` - Liquid-based
- `"Salad"` - Fresh vegetables
- `"Curry"` - Spiced sauce
- `"Stew"` - Slow-cooked

---

## 💡 Tips for Adding Great Recipes

### 1. **Use Common Ingredients**
Focus on ingredients people usually have:
- ✅ eggs, cheese, bread, tomato, onion, garlic, rice, pasta
- ❌ truffle oil, saffron threads, exotic spices

### 2. **Be Flexible with Ingredient Names**
The app matches similar ingredients automatically:
- "egg" matches "eggs"
- "tomato" matches "tomatoes"
- "onion" matches "onions"

### 3. **Include Popular Dishes**
Add recipes people actually want to make:
- ✅ Spaghetti, Pizza, Tacos, Fried Rice
- ❌ Obscure regional dishes few people know

### 4. **Vary Cooking Times**
Include quick and slow recipes:
- Quick: 5-15 minutes (Omelette, Toast, Salad)
- Medium: 20-40 minutes (Curry, Stir-fry, Pasta)
- Slow: 45+ minutes (Biryani, Lasagna, Stew)

### 5. **Add Dietary Variety**
Include options for different diets:
- Vegetarian: Use beans, tofu, paneer
- Vegan: No animal products
- Gluten-free: Use rice, potatoes instead of wheat
- Quick: For busy people

---

## 🌟 Example Recipe Ideas to Add

### Asian
- Ramen, Udon, Sushi Rolls, Dumplings, Curry, Satay

### European
- Schnitzel (German), Pierogi (Polish), Goulash (Hungarian), Borscht (Russian)

### Middle Eastern
- Shawarma, Tabbouleh, Falafel Wrap, Shakshuka

### Latin American
- Empanadas, Ceviche, Arepas, Pupusas

### African
- Jollof Rice, Couscous, Tagine, Injera

### Comfort Food
- Pot Roast, Chicken & Dumplings, Beef Stew, Potato Casserole

### Quick Meals
- Instant Noodles (elevated), Microwave Mug Cakes, 5-Minute Salads

---

## 🧪 Testing Your New Recipes

After adding recipes, test them:

```bash
# Test with your new recipe ingredients
python app.py find "beef, onion, bell peppers"

# Or use the GUI
python gui.py
```

---

## 📦 Sharing Your Recipes

Want to share your expanded recipe library?

1. **Backup your file**: Copy `providers/fallback_recipes.py`
2. **Share with others**: They can replace their file with yours
3. **Contribute**: Consider sharing popular recipes with the community!

---

## 🎯 Recipe Template (Copy & Paste)

```python
    {
        "id": "fallback_XXX",  # Use next available number
        "title": "Recipe Name Here",
        "cuisine": "Cuisine Name",
        "category": ["Category1", "Category2"],
        "ingredients": [
            "ingredient 1",
            "ingredient 2",
            "ingredient 3",
            "ingredient 4"
        ],
        "time": 30,  # minutes
        "servings": 4,
        "instructions": "How to make this dish."
    },
```

---

## 🚀 Advanced: Bulk Recipe Import

For adding MANY recipes at once, you can:

1. Create a JSON/CSV file with your recipes
2. Write a simple Python script to convert them
3. Append to `FALLBACK_RECIPES` list

Example converter script:
```python
import json

# Your recipes in JSON format
with open('my_recipes.json', 'r') as f:
    new_recipes = json.load(f)

# Print formatted for fallback_recipes.py
for i, recipe in enumerate(new_recipes, start=71):
    print(f'''    {{
        "id": "fallback_{i:03d}",
        "title": "{recipe['title']}",
        "cuisine": "{recipe['cuisine']}",
        "category": {recipe['category']},
        "ingredients": {recipe['ingredients']},
        "time": {recipe['time']},
        "servings": {recipe['servings']},
        "instructions": "{recipe['instructions']}"
    }},''')
```

---

## 📊 Current Stats

- **Total Recipes**: 70
- **Cuisines Covered**: 15+
- **Average Cooking Time**: ~28 minutes
- **Quickest Recipe**: Avocado Toast (5 min)
- **Longest Recipe**: Moussaka, Lasagna (90 min)
- **Most Ingredients**: Paella (7 items)
- **Fewest Ingredients**: Avocado Toast (6 items)

---

## 🎉 Your Library Keeps Growing!

Every recipe you add makes the app more useful for everyone. Happy cooking! 🍳👨‍🍳👩‍🍳

# 🖥️ GUI User Guide

## Quick Start

### Launch the GUI

**Windows:**
- Double-click `START_GUI.bat`
- Or run: `python gui.py`

**Mac/Linux:**
- Run: `./START_GUI.sh` (after `chmod +x START_GUI.sh`)
- Or run: `python3 gui.py`

---

## GUI Overview

```
┌─────────────────────────────────────────────────┐
│  🍳 Recipe Finder                                │
├─────────────────────────────────────────────────┤
│                                                  │
│  🔍 Ingredients                                  │
│  ┌────────────────────────────────────────┐     │
│  │ egg, cheese, tomato           [Search] │     │
│  └────────────────────────────────────────┘     │
│                                                  │
│  ⚙️ Filters                                      │
│  Provider: [themealdb ▾]  Max Results: [10]     │
│  Diet: [vegetarian ▾]     Max Time: [30]        │
│  Sort by: [used-desc ▾]                          │
│                                                  │
│  📋 Results                                      │
│  ┌────────────────────────────────────────┐     │
│  │ ☑ Spanish Omelette    100%  2  0  -   │     │
│  │ ☐ Shakshuka            67%  2  1  25m  │     │
│  └────────────────────────────────────────┘     │
│                                                  │
│  📝 Recipe Details                               │
│  ┌────────────────────────────────────────┐     │
│  │ Selected recipe details appear here... │     │
│  │ • Ingredients you have                  │     │
│  │ • Ingredients you need                  │     │
│  │ • Instructions link                     │     │
│  └────────────────────────────────────────┘     │
│                                                  │
│  [📁 Export] [🔗 View Online] [🗑️ Clear]        │
│                                    Status: Ready │
└─────────────────────────────────────────────────┘
```

---

## Step-by-Step Guide

### 1. Enter Ingredients
- Type ingredients in the text box (comma-separated)
- Example: `egg, cheese, tomato`
- Press **Enter** or click **Search Recipes**

### 2. Apply Filters (Optional)
- **Provider**: Choose API source
  - `themealdb` - Free, no API key needed (default)
  - `spoonacular` - Budget features (needs API key)
  - `edamam` - Nutrition focus (needs API key)

- **Max Results**: How many recipes to show (1-50)

- **Diet**: Filter by dietary preference
  - vegetarian, vegan, gluten-free, ketogenic, paleo

- **Max Time**: Maximum cooking time in minutes

- **Sort by**: How to order results
  - `used-desc` - Most ingredients you have (default)
  - `missing-asc` - Fewest ingredients you need
  - `cost-asc` - Cheapest first (Spoonacular only)
  - `time-asc` - Fastest first

### 3. Browse Results
- Results appear in the table
- Click any recipe to see details
- Details show:
  - ✓ Ingredients you have
  - ⚠ Ingredients you need
  - Match percentage
  - Cooking time & servings
  - Recipe URL

### 4. View Recipe
- Click **🔗 View Recipe Online** to open in browser
- Opens the full recipe with instructions

### 5. Export Results
- Click **📁 Export Results**
- Choose format:
  - JSON - For data/programming
  - CSV - For spreadsheets
  - HTML - For viewing in browser
- Select location and save

### 6. Clear & Start Over
- Click **🗑️ Clear** to reset everything
- Enter new ingredients and search again

---

## Tips & Tricks

### 🎯 For Best Results

1. **Start Simple**
   - Use 2-3 main ingredients
   - Example: `chicken, rice` instead of listing everything

2. **Use TheMealDB First**
   - No setup required
   - Good for testing

3. **Try Different Providers**
   - Each has different recipes
   - Spoonacular for budget info
   - Edamam for health-conscious

4. **Check Match %**
   - 100% = You have everything
   - 80%+ = Usually easy to make
   - <50% = Many missing ingredients

5. **Export Favorites**
   - Save recipes you like to HTML
   - Create your own cookbook

### ⚙️ Provider Setup

**To use Spoonacular or Edamam:**

1. Copy `.env.example` to `.env`
2. Get API keys:
   - Spoonacular: https://spoonacular.com/food-api
   - Edamam: https://developer.edamam.com/
3. Add keys to `.env` file:
   ```
   SPOONACULAR_API_KEY=your_key_here
   EDAMAM_APP_ID=your_id_here
   EDAMAM_APP_KEY=your_key_here
   ```
4. Restart GUI
5. Select provider in dropdown

---

## Keyboard Shortcuts

- **Enter** in ingredients box → Search
- **Double-click** recipe → View details
- **Escape** → Close GUI

---

## Troubleshooting

### "No recipes found"
- ✓ Try fewer ingredients
- ✓ Check spelling
- ✓ Remove filters
- ✓ Try different provider

### "Search failed"
- ✓ Check internet connection
- ✓ If using Spoonacular/Edamam, check API keys in `.env`
- ✓ Try TheMealDB instead

### GUI won't start
- ✓ Install dependencies: `pip install -r requirements.txt`
- ✓ Check Python installed: `python --version`
- ✓ Must be Python 3.7 or higher

### Filters not working
- ✓ Diet/health filters require Spoonacular or Edamam
- ✓ TheMealDB has limited filter support
- ✓ Time filter only works if provider returns time data

---

## GUI Features

### ✅ What Works
- ✓ All providers (TheMealDB, Spoonacular, Edamam)
- ✓ All filters (diet, time, sort)
- ✓ Recipe details display
- ✓ Export to JSON/CSV/HTML
- ✓ Open recipes in browser
- ✓ Responsive window
- ✓ Scrollable results
- ✓ Status updates

### 🔮 Future Enhancements
- Recipe favorites/bookmarks
- Ingredient history
- Dark mode
- Recipe images in grid view
- Print recipes
- Share recipes

---

## Comparison: CLI vs GUI

| Feature | CLI | GUI |
|---------|-----|-----|
| **Ease of Use** | Commands | Point & click |
| **Speed** | Faster for experts | Easier for beginners |
| **Features** | All features | All features |
| **Visual** | Text tables | Interactive windows |
| **Automation** | Scripts | Manual |
| **Best For** | Power users | Everyone |

**Both interfaces use the same underlying engine!**

---

## Example Searches

### Easy Breakfast
```
Ingredients: egg, bread, cheese
Filters: Max Time = 15
```

### Healthy Lunch
```
Ingredients: chicken, vegetables
Filters: Diet = vegetarian, Sort = missing-asc
```

### Budget Dinner
```
Ingredients: rice, beans, tomato
Provider: spoonacular
Filters: Sort = cost-asc
```

### Quick Snack
```
Ingredients: cheese, crackers
Filters: Max Time = 10
```

---

## Getting Help

- **User Guide**: This file
- **Full Documentation**: README.md
- **Quick Start**: QUICKSTART.md
- **Examples**: examples.py
- **Issues**: Open an issue on GitHub

---

**Happy Cooking with GUI! 🍳✨**

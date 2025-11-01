# 🍳 R## ✨ Features

- **🖥️ Dual Interface**: Choose CLI or GUI - both included!
- **🔍 Ingredient-Based Search**: Enter what you have, find what you can make
- **🌍 International Recipes**: 70+ built-in recipes from 15+ cuisines (Indian, Mexican, Thai, Korean, Greek, Vietnamese, Spanish, and more!)
- **✅ Always Get Results**: Fallback recipe database ensures you always find something to cook
- **➕ Expandable**: Easy to add your own recipes - just edit one file!
- **💰 Budget-Aware**: Filter by cost per serving (Spoonacular only)
- **⏱️ Time-Conscious**: Filter by cooking time
- **🥗 Diet & Health Filters**: Vegetarian, vegan, gluten-free, nut-free, etc.
- **📊 Smart Matching**: See what ingredients you have vs. what you need
- **📁 Export**: Save recipes to JSON, CSV, or HTML cookbook
- **🎨 Beautiful Output**: Rich CLI tables or intuitive GUIer

> Find recipes based on ingredients you already have, with optional filters for diet, budget, and cooking time.

A beginner-friendly Python application (CLI + GUI) that helps you discover recipes using leftover ingredients. No more wondering "what can I make with these random ingredients?"

## ✨ Features

- **�️ Dual Interface**: Choose CLI or GUI - both included!
- **�🔍 Ingredient-Based Search**: Enter what you have, find what you can make
- **💰 Budget-Aware**: Filter by cost per serving (Spoonacular only)
- **⏱️ Time-Conscious**: Filter by cooking time
- **🥗 Diet & Health Filters**: Vegetarian, vegan, gluten-free, nut-free, etc.
- **📊 Smart Matching**: See what ingredients you have vs. what you need
- **📁 Export**: Save recipes to JSON, CSV, or HTML cookbook
- **🎨 Beautiful Output**: Rich CLI tables or intuitive GUI

## 🎯 Quick Start (No API Key Required!)

### 1. Installation

```bash
# Clone or download this repository
cd FoodRecepie

# Install dependencies
pip install -r requirements.txt
```

### 2. Choose Your Interface

**Option A: Graphical Interface (Recommended for beginners)**
```bash
python gui.py
```
A user-friendly window will open where you can:
- Enter ingredients
- Select filters with dropdowns
- View results in a nice table
- Click to see recipe details
- Export with one click

**Option B: Command Line Interface**
```bash
# Search with TheMealDB (no API key needed!)
python app.py find "egg, tomato, onion"
```

That's it! The app uses TheMealDB's free tier by default.

## 📋 Requirements

- Python 3.7+
- `requests` - HTTP library
- `python-dotenv` - Environment variable management
- `rich` - Beautiful terminal formatting

Install all at once:
```bash
pip install -r requirements.txt
```

## 🚀 Usage Examples

### Basic Search
```bash
# Find recipes with eggs and tomatoes
python app.py find "egg, tomato"

# Search with multiple ingredients
python app.py find "chicken, rice, onion, garlic"
```

### With Filters
```bash
# Vegetarian recipes under 30 minutes
python app.py find "pasta, tomato" --diet vegetarian --max-mins 30

# Budget-friendly recipes (requires Spoonacular)
python app.py find "rice, beans" --provider spoonacular --max-cost 2.00

# Exclude ingredients
python app.py find "chicken, potato" --exclude "garlic, onion"
```

### Export Results
```bash
# Export to JSON
python app.py find "egg, cheese" --export results.json

# Export to CSV
python app.py find "pasta, tomato" --export results.csv

# Export to HTML cookbook
python app.py find "chicken, rice" --export cookbook.html
```

### Sort Results
```bash
# Maximize used ingredients (default)
python app.py find "egg, tomato" --sort used-desc

# Minimize missing ingredients
python app.py find "egg, tomato" --sort missing-asc

# Lowest cost first (Spoonacular only)
python app.py find "rice, beans" --provider spoonacular --sort cost-asc

# Shortest time first
python app.py find "pasta, tomato" --sort time-asc
```

## 🔌 API Providers

### TheMealDB (Default - Free!)

**No configuration needed!** Uses the free test key automatically.

**Features:**
- ✅ Ingredient-based search
- ✅ Recipe details with instructions
- ✅ Categories and cuisines
- ❌ No cost information
- ❌ No cooking time
- ❌ Limited diet filters

**Usage:**
```bash
python app.py find "chicken, rice"
```

### Spoonacular (Premium Features)

**Requires API key** - [Get one here](https://spoonacular.com/food-api)

**Features:**
- ✅ "What's in your fridge" search
- ✅ Used vs. missing ingredients
- ✅ Cost per serving
- ✅ Cooking time
- ✅ Diet filters (vegetarian, vegan, etc.)
- ✅ Price breakdown

**Setup:**
1. Create a `.env` file (copy from `.env.example`)
2. Add your API key:
   ```
   SPOONACULAR_API_KEY=your_key_here
   ```

**Usage:**
```bash
python app.py find "egg, tomato" --provider spoonacular --max-cost 2.00
```

### Edamam (Nutrition Focus)

**Requires API credentials** - [Get them here](https://developer.edamam.com/)

**Features:**
- ✅ Strong diet/health filters
- ✅ Nutrition information
- ✅ Multiple health labels
- ✅ Cooking time
- ❌ No cost information
- ❌ Instructions link to external sites

**Setup:**
1. Create a `.env` file (copy from `.env.example`)
2. Add your credentials:
   ```
   EDAMAM_APP_ID=your_app_id
   EDAMAM_APP_KEY=your_app_key
   ```

**Usage:**
```bash
python app.py find "chicken" --provider edamam --diet vegetarian --health nut-free
```

## 🎛️ Command Reference

### Find Command

```bash
python app.py find <ingredients> [options]
```

**Arguments:**
- `ingredients` - Comma-separated list (required)

**Options:**
- `--provider {themealdb|spoonacular|edamam}` - API provider (default: themealdb)
- `--max-mins INT` - Maximum cooking time in minutes
- `--diet {vegetarian|vegan|gluten-free|ketogenic|paleo}` - Dietary preference
- `--health {nut-free|dairy-free|egg-free|soy-free|fish-free}` - Health restrictions (can use multiple)
- `--exclude INGREDIENTS` - Comma-separated ingredients to exclude
- `--max-cost FLOAT` - Maximum cost per serving in USD (Spoonacular only)
- `--limit INT` - Maximum number of results (default: 10)
- `--sort {used-desc|missing-asc|cost-asc|time-asc}` - Sort method (default: used-desc)
- `--export FILE` - Export results to file

### Export Command

```bash
python app.py export <output_file> [--format {json|csv|html}]
```

Exports the last search results to a file. Format is auto-detected from file extension.

## 📂 Project Structure

```
FoodRecepie/
├── app.py                  # Main CLI entry point
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment config
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── core/                  # Core business logic
│   ├── __init__.py
│   ├── model.py          # Recipe data model
│   ├── normalize.py      # Ingredient normalization
│   ├── orchestrator.py   # Provider routing
│   ├── sorters.py        # Sorting & filtering
│   └── export.py         # Export functionality
├── providers/             # API provider implementations
│   ├── __init__.py
│   ├── themealdb.py      # TheMealDB provider
│   ├── spoonacular.py    # Spoonacular provider
│   └── edamam.py         # Edamam provider
├── ui/                    # User interface
│   ├── __init__.py
│   └── cli.py            # CLI with Rich formatting
└── tests/                 # Unit tests
    ├── __init__.py
    ├── test_normalize.py
    └── test_sorters.py
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests.test_normalize

# Run with verbose output
python -m unittest discover tests -v
```

## 🎨 Output Examples

### Table View
```
╭────────────────────────────────────────── 🍳 Recipe Results ──────────────────────────────────────────╮
│ #  │ Title                        │ Match  │ Have              │ Need              │ Time │ Cost   │ Provider  │
├────┼──────────────────────────────┼────────┼───────────────────┼───────────────────┼──────┼────────┼───────────┤
│ 1  │ Spanish Omelette             │ 100%   │ egg, tomato       │ -                 │ -    │ -      │ themealdb │
│ 2  │ Shakshuka                    │ 67%    │ egg, tomato       │ onion             │ -    │ -      │ themealdb │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Recipe Details
```
┌─────────────────────────────────────────┐
│          Spanish Omelette                │
└─────────────────────────────────────────┘
  🌍 Cuisine: Spanish | 🍽️ Servings: 4 | ⏱️ Time: 25 minutes

  Match: 100% (2 have / 0 need)

  ✓ Ingredients you have:
    • Egg
    • Tomato

  📝 Full ingredient list:
    • 4 Egg
    • 2 Tomato
    • Salt and pepper to taste
```

## 🔧 Configuration

Create a `.env` file in the project root (copy from `.env.example`):

```env
# TheMealDB uses test key "1" by default (no configuration needed)

# Spoonacular API (optional)
SPOONACULAR_API_KEY=your_key_here

# Edamam API (optional)
EDAMAM_APP_ID=your_app_id_here
EDAMAM_APP_KEY=your_app_key_here

# Default provider
PROVIDER=themealdb
```

## 🚧 Limitations & Known Issues

### TheMealDB
- ❌ Multi-ingredient filtering is a premium feature - we work around this by intersecting results locally
- ❌ No cost information
- ❌ No cooking time data
- ✅ Free tier is very generous

### Spoonacular
- ⚠️ Free tier has limited API calls (150/day)
- ⚠️ Some recipes may not have price data
- ✅ Best for "what's in your fridge" search
- ✅ Most comprehensive feature set

### Edamam
- ⚠️ Free tier has limited calls (10/min, 10,000/month)
- ❌ No instructions (links to external sites)
- ❌ No cost information
- ✅ Best for diet/nutrition filters
- ✅ Large recipe database

## 🛣️ Roadmap

### v1.1 (Planned)
- [ ] Simple Tkinter GUI
- [ ] Pantry mode (save staple ingredients)
- [ ] Favorites list (local storage)
- [ ] Recipe rating/notes

### v1.2 (Future)
- [ ] Shopping list generator from missing ingredients
- [ ] Meal planning
- [ ] Nutrition tracking
- [ ] Recipe scaling (adjust servings)

## 🤝 Contributing

This is a learning project! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your recipes

## 📄 License

MIT License - Use freely for personal and commercial projects.

## 🙏 Credits

**APIs Used:**
- [TheMealDB](https://www.themealdb.com/) - Free recipe database
- [Spoonacular](https://spoonacular.com/food-api) - Comprehensive food API
- [Edamam](https://www.edamam.com/) - Nutrition & recipe search

**Libraries:**
- [Rich](https://github.com/Textualize/rich) - Terminal formatting
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment management

## 💡 Tips & Tricks

1. **Start Simple**: Use TheMealDB with basic ingredients to get familiar
2. **Be Specific**: "chicken breast" works better than just "meat"
3. **Use Exclusions**: `--exclude "garlic, onion"` if you don't like them
4. **Export Often**: Save interesting recipes for later
5. **Mix Providers**: TheMealDB for quick searches, Spoonacular when you need cost info
6. **Check Match %**: Recipes with 80%+ match are usually easy to make

## 🆘 Troubleshooting

### "No recipes found"
- Try fewer ingredients
- Check spelling
- Remove very specific ingredients
- Try a different provider

### "API key not configured"
- Make sure `.env` file exists
- Check API key is correct
- Verify you copied `.env.example` to `.env`

### "Request failed"
- Check internet connection
- Verify API key is valid and not expired
- You may have hit rate limits (wait a minute)

### Import errors
- Run `pip install -r requirements.txt`
- Check Python version (3.7+ required)
- Make sure you're in the project directory

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues first
- Include error messages and steps to reproduce

---

**Happy Cooking! 🍳👨‍🍳👩‍🍳**

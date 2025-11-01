# Quick Start Guide

## 🚀 Get Started in 60 Seconds

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Your First Search
```bash
python app.py find "egg, tomato"
```

That's it! No API keys needed for basic usage.

## 📝 Common Commands

### Search Examples
```bash
# Basic search
python app.py find "chicken, rice, onion"

# With time limit
python app.py find "pasta, tomato" --max-mins 30

# Vegetarian only
python app.py find "tofu, vegetables" --diet vegetarian

# Export to file
python app.py find "egg, cheese" --export my_recipes.json
```

### Get Help
```bash
# General help
python app.py --help

# Command-specific help
python app.py find --help
python app.py export --help
```

## 🎯 What to Try

1. **Start Simple**: `python app.py find "egg, cheese"`
2. **Add Filters**: `python app.py find "egg, cheese" --max-mins 20`
3. **Export Results**: `python app.py find "pasta" --export recipes.html`
4. **Open the HTML**: Open `recipes.html` in your browser for a nice cookbook view

## ⚙️ Optional: Enable Premium Features

### For Budget & Cost Info (Spoonacular)
1. Get a free API key from https://spoonacular.com/food-api
2. Copy `.env.example` to `.env`
3. Add your key to `.env`:
   ```
   SPOONACULAR_API_KEY=your_key_here
   ```
4. Use it:
   ```bash
   python app.py find "rice, beans" --provider spoonacular --max-cost 2.00
   ```

### For Nutrition Filters (Edamam)
1. Get credentials from https://developer.edamam.com/
2. Add to `.env`:
   ```
   EDAMAM_APP_ID=your_id
   EDAMAM_APP_KEY=your_key
   ```
3. Use it:
   ```bash
   python app.py find "chicken" --provider edamam --health nut-free
   ```

## 🐛 Troubleshooting

**"No module named 'X'"**
→ Run: `pip install -r requirements.txt`

**"No recipes found"**
→ Try fewer ingredients or simpler terms

**Export doesn't work**
→ Make sure you've run a search first

## 📖 Next Steps

- Read the full README.md for all features
- Try different providers (themealdb, spoonacular, edamam)
- Experiment with filters (diet, time, cost)
- Export your favorite recipes to keep them

**Happy cooking! 🍳**

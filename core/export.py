"""Export recipes to various formats"""
import json
import csv
from typing import List
from pathlib import Path
from core.model import Recipe

def export_to_json(recipes: List[Recipe], filepath: str) -> None:
    """
    Export recipes to JSON format.
    
    Args:
        recipes: List of recipes to export
        filepath: Output file path
    """
    data = {
        "count": len(recipes),
        "recipes": [r.to_dict() for r in recipes]
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Exported {len(recipes)} recipes to {filepath}")

def export_to_csv(recipes: List[Recipe], filepath: str) -> None:
    """
    Export recipes to CSV format.
    
    Args:
        recipes: List of recipes to export
        filepath: Output file path
    """
    if not recipes:
        print("No recipes to export")
        return
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'id', 'provider', 'title', 'image_url', 'source_url',
            'used_ingredients', 'missing_ingredients',
            'match_percentage', 'servings', 'ready_in_minutes',
            'cuisine', 'cost_per_serving_usd'
        ]
        
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for recipe in recipes:
            row = {
                'id': recipe.id,
                'provider': recipe.provider.value,
                'title': recipe.title,
                'image_url': recipe.image_url or '',
                'source_url': recipe.source_url or '',
                'used_ingredients': '; '.join(recipe.used_ingredients),
                'missing_ingredients': '; '.join(recipe.missing_ingredients),
                'match_percentage': round(recipe.match_percentage, 1),
                'servings': recipe.servings or '',
                'ready_in_minutes': recipe.ready_in_minutes or '',
                'cuisine': recipe.cuisine or '',
                'cost_per_serving_usd': recipe.cost_per_serving_usd or ''
            }
            writer.writerow(row)
    
    print(f"✓ Exported {len(recipes)} recipes to {filepath}")

def export_to_html(recipes: List[Recipe], filepath: str) -> None:
    """
    Export recipes to HTML format (simple cookbook).
    
    Args:
        recipes: List of recipes to export
        filepath: Output file path
    """
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Collection</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 40px;
        }
        .recipe-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 20px;
        }
        .recipe-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .recipe-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .recipe-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .recipe-content {
            padding: 20px;
        }
        .recipe-title {
            font-size: 1.4em;
            margin: 0 0 10px 0;
            color: #2c3e50;
        }
        .recipe-meta {
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 15px;
        }
        .recipe-meta span {
            margin-right: 15px;
        }
        .ingredients {
            margin: 15px 0;
        }
        .ingredients-title {
            font-weight: bold;
            color: #27ae60;
            margin-bottom: 5px;
        }
        .ingredient-list {
            font-size: 0.9em;
            color: #555;
        }
        .missing {
            color: #e74c3c;
            font-weight: bold;
        }
        .match-badge {
            display: inline-block;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: bold;
            background-color: #3498db;
            color: white;
            margin-top: 10px;
        }
        .link-button {
            display: inline-block;
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.9em;
        }
        .link-button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <h1>🍳 Recipe Collection</h1>
    <div class="recipe-grid">
"""
    
    for recipe in recipes:
        html += f"""
        <div class="recipe-card">
            <img class="recipe-image" src="{recipe.image_url or 'https://via.placeholder.com/350x200?text=No+Image'}" alt="{recipe.title}">
            <div class="recipe-content">
                <h2 class="recipe-title">{recipe.title}</h2>
                <div class="recipe-meta">
                    {f'<span>⏱️ {recipe.ready_in_minutes} min</span>' if recipe.ready_in_minutes else ''}
                    {f'<span>🍽️ {recipe.servings} servings</span>' if recipe.servings else ''}
                    {f'<span>💰 ${recipe.cost_per_serving_usd:.2f}/serving</span>' if recipe.cost_per_serving_usd else ''}
                </div>
                <div class="ingredients">
                    <div class="ingredients-title">✓ You have ({len(recipe.used_ingredients)}):</div>
                    <div class="ingredient-list">{', '.join(recipe.used_ingredients[:5])}{' ...' if len(recipe.used_ingredients) > 5 else ''}</div>
                </div>
        """
        
        if recipe.missing_ingredients:
            html += f"""
                <div class="ingredients">
                    <div class="ingredients-title missing">⚠ You need ({len(recipe.missing_ingredients)}):</div>
                    <div class="ingredient-list">{', '.join(recipe.missing_ingredients[:5])}{' ...' if len(recipe.missing_ingredients) > 5 else ''}</div>
                </div>
            """
        
        html += f"""
                <span class="match-badge">{recipe.match_percentage:.0f}% Match</span>
                {f'<a href="{recipe.source_url}" class="link-button" target="_blank">View Recipe →</a>' if recipe.source_url else ''}
            </div>
        </div>
        """
    
    html += """
    </div>
</body>
</html>
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Exported {len(recipes)} recipes to {filepath}")

def export_recipes(recipes: List[Recipe], filepath: str, format: str = None) -> None:
    """
    Export recipes to file in specified format.
    
    Args:
        recipes: List of recipes to export
        filepath: Output file path
        format: Output format (json, csv, html) - auto-detected if None
    """
    if not recipes:
        print("No recipes to export")
        return
    
    # Auto-detect format from extension if not specified
    if format is None:
        ext = Path(filepath).suffix.lower()
        if ext == '.json':
            format = 'json'
        elif ext == '.csv':
            format = 'csv'
        elif ext in ['.html', '.htm']:
            format = 'html'
        else:
            format = 'json'  # Default
    
    # Export based on format
    if format == 'json':
        export_to_json(recipes, filepath)
    elif format == 'csv':
        export_to_csv(recipes, filepath)
    elif format == 'html':
        export_to_html(recipes, filepath)
    else:
        raise ValueError(f"Unsupported export format: {format}")

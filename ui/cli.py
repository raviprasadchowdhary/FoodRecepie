"""CLI interface with Rich formatting"""
from typing import List, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from core.model import Recipe
from core.orchestrator import search_recipes as orchestrator_search
from core.export import export_recipes

console = Console()

# Store last search results for export command
_last_results: List[Recipe] = []

def format_ingredient_list(ingredients: List[str], max_items: int = 3) -> str:
    """Format ingredient list for display"""
    if not ingredients:
        return "-"
    
    if len(ingredients) <= max_items:
        return ", ".join(ingredients)
    else:
        shown = ", ".join(ingredients[:max_items])
        return f"{shown} (+{len(ingredients) - max_items} more)"

def display_recipes_table(recipes: List[Recipe]) -> None:
    """Display recipes in a formatted table"""
    if not recipes:
        console.print("[yellow]No recipes found matching your criteria.[/yellow]")
        return
    
    table = Table(
        title="🍳 Recipe Results",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta"
    )
    
    table.add_column("#", style="dim", width=3)
    table.add_column("Title", style="cyan", width=30)
    table.add_column("Match", justify="center", width=8)
    table.add_column("Have", style="green", width=20)
    table.add_column("Need", style="red", width=20)
    table.add_column("Time", justify="center", width=8)
    table.add_column("Cost", justify="right", width=8)
    table.add_column("Provider", style="dim", width=10)
    
    for idx, recipe in enumerate(recipes, 1):
        # Format match percentage with color
        match_pct = recipe.match_percentage
        if match_pct >= 80:
            match_color = "green"
        elif match_pct >= 50:
            match_color = "yellow"
        else:
            match_color = "red"
        match_str = f"[{match_color}]{match_pct:.0f}%[/{match_color}]"
        
        # Format time
        time_str = f"{recipe.ready_in_minutes}m" if recipe.ready_in_minutes else "-"
        
        # Format cost
        cost_str = f"${recipe.cost_per_serving_usd:.2f}" if recipe.cost_per_serving_usd else "-"
        
        # Format ingredient lists
        have_str = format_ingredient_list(recipe.used_ingredients, 2)
        need_str = format_ingredient_list(recipe.missing_ingredients, 2)
        
        table.add_row(
            str(idx),
            recipe.title[:30],
            match_str,
            have_str,
            need_str,
            time_str,
            cost_str,
            recipe.provider.value
        )
    
    console.print(table)
    console.print(f"\n[dim]Found {len(recipes)} recipes[/dim]")

def display_recipe_details(recipe: Recipe, index: int) -> None:
    """Display detailed information for a single recipe"""
    # Title panel
    title_text = Text(recipe.title, style="bold cyan", justify="center")
    console.print(Panel(title_text, border_style="cyan"))
    
    # Meta information
    meta_info = []
    if recipe.cuisine:
        meta_info.append(f"🌍 Cuisine: {recipe.cuisine}")
    if recipe.servings:
        meta_info.append(f"🍽️  Servings: {recipe.servings}")
    if recipe.ready_in_minutes:
        meta_info.append(f"⏱️  Time: {recipe.ready_in_minutes} minutes")
    if recipe.cost_per_serving_usd:
        meta_info.append(f"💰 Cost: ${recipe.cost_per_serving_usd:.2f}/serving")
    
    if meta_info:
        console.print("  " + " | ".join(meta_info))
        console.print()
    
    # Match info
    match_pct = recipe.match_percentage
    match_color = "green" if match_pct >= 80 else "yellow" if match_pct >= 50 else "red"
    console.print(f"  [{match_color}]Match: {match_pct:.0f}%[/{match_color}] "
                  f"([green]{len(recipe.used_ingredients)} have[/green] / "
                  f"[red]{len(recipe.missing_ingredients)} need[/red])")
    console.print()
    
    # Ingredients you have
    if recipe.used_ingredients:
        console.print("  [bold green]✓ Ingredients you have:[/bold green]")
        for ing in recipe.used_ingredients:
            console.print(f"    • {ing}")
        console.print()
    
    # Ingredients you need
    if recipe.missing_ingredients:
        console.print("  [bold red]⚠ Ingredients you need:[/bold red]")
        for ing in recipe.missing_ingredients:
            console.print(f"    • {ing}")
        console.print()
    
    # All ingredients with measures
    if recipe.ingredients:
        console.print("  [bold]📝 Full ingredient list:[/bold]")
        for ing in recipe.ingredients:
            console.print(f"    • {ing}")
        console.print()
    
    # Instructions link
    if recipe.source_url:
        console.print(f"  [bold]🔗 Recipe link:[/bold] [link={recipe.source_url}]{recipe.source_url}[/link]")
        console.print()
    
    # Categories/tags
    if recipe.category_or_diet:
        console.print(f"  [dim]Tags: {', '.join(recipe.category_or_diet)}[/dim]")
        console.print()

def handle_find_command(args) -> int:
    """Handle the 'find' command"""
    global _last_results
    
    try:
        console.print(f"\n[bold]Searching for recipes with: {args.ingredients}[/bold]")
        
        if args.provider != 'themealdb':
            console.print(f"[dim]Using provider: {args.provider}[/dim]")
        
        # Search for recipes
        recipes = orchestrator_search(
            ingredients_str=args.ingredients,
            provider=args.provider,
            max_results=args.limit,
            diet=args.diet,
            health=args.health,
            max_minutes=args.max_mins,
            max_cost=args.max_cost,
            exclude_str=args.exclude,
            sort_by=args.sort
        )
        
        # Store results for export
        _last_results = recipes
        
        # Display results
        console.print()
        display_recipes_table(recipes)
        
        # Show details if only a few results
        if recipes and len(recipes) <= 3:
            console.print("\n[bold]Recipe Details:[/bold]\n")
            for idx, recipe in enumerate(recipes, 1):
                display_recipe_details(recipe, idx)
                if idx < len(recipes):
                    console.print("─" * 80)
                    console.print()
        
        # Export if requested
        if args.export and recipes:
            export_recipes(recipes, args.export)
        
        return 0
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return 1

def handle_export_command(args) -> int:
    """Handle the 'export' command"""
    global _last_results
    
    if not _last_results:
        console.print("[yellow]No recipes to export. Run a search first.[/yellow]")
        return 1
    
    try:
        export_recipes(_last_results, args.output, args.format)
        return 0
    except Exception as e:
        console.print(f"[bold red]Error exporting:[/bold red] {e}")
        return 1

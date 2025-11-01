#!/usr/bin/env python3
"""
Recipe Finder - Find recipes based on ingredients you have
"""
import argparse
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main entry point for the recipe finder CLI"""
    parser = argparse.ArgumentParser(
        description='Find recipes based on ingredients you have',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py find "egg, tomato, onion"
  python app.py find "chicken, rice" --provider spoonacular --max-mins 30
  python app.py find "pasta, tomato" --diet vegetarian --max-cost 2.00
  python app.py export results.json --format json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Find command
    find_parser = subparsers.add_parser('find', help='Search for recipes by ingredients')
    find_parser.add_argument(
        'ingredients',
        type=str,
        help='Comma-separated list of ingredients (e.g., "egg, tomato, onion")'
    )
    find_parser.add_argument(
        '--provider',
        type=str,
        choices=['themealdb', 'spoonacular', 'edamam'],
        default=os.getenv('PROVIDER', 'themealdb'),
        help='API provider to use (default: themealdb)'
    )
    find_parser.add_argument(
        '--max-mins',
        type=int,
        help='Maximum cooking time in minutes'
    )
    find_parser.add_argument(
        '--diet',
        type=str,
        choices=['vegetarian', 'vegan', 'gluten-free', 'ketogenic', 'paleo'],
        help='Dietary preference'
    )
    find_parser.add_argument(
        '--health',
        type=str,
        action='append',
        choices=['nut-free', 'dairy-free', 'egg-free', 'soy-free', 'fish-free'],
        help='Health restrictions (can specify multiple times)'
    )
    find_parser.add_argument(
        '--exclude',
        type=str,
        help='Comma-separated list of ingredients to exclude'
    )
    find_parser.add_argument(
        '--max-cost',
        type=float,
        help='Maximum cost per serving in USD (Spoonacular only)'
    )
    find_parser.add_argument(
        '--limit',
        type=int,
        default=10,
        help='Maximum number of results to return (default: 10)'
    )
    find_parser.add_argument(
        '--sort',
        type=str,
        choices=['used-desc', 'missing-asc', 'cost-asc', 'time-asc'],
        default='used-desc',
        help='How to sort results (default: used-desc)'
    )
    find_parser.add_argument(
        '--export',
        type=str,
        help='Export results to file (e.g., results.json or results.csv)'
    )
    
    # Export command (for exporting previously found recipes)
    export_parser = subparsers.add_parser('export', help='Export recipes to file')
    export_parser.add_argument(
        'output',
        type=str,
        help='Output file path (extension determines format: .json, .csv, .html)'
    )
    export_parser.add_argument(
        '--format',
        type=str,
        choices=['json', 'csv', 'html'],
        help='Output format (auto-detected from file extension if not specified)'
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    # Import UI module here to avoid circular imports
    from ui.cli import handle_find_command, handle_export_command
    
    if args.command == 'find':
        return handle_find_command(args)
    elif args.command == 'export':
        return handle_export_command(args)
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

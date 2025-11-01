"""
Recipe Finder - Modern Aesthetic GUI
A beautiful, modern graphical interface for finding recipes
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from typing import List, Optional
import webbrowser

from core.orchestrator import search_recipes
from core.export import export_recipes
from core.model import Recipe
from providers.fallback_recipes import FALLBACK_RECIPES


class ModernRecipeFinderGUI:
    """Modern, aesthetic GUI application for Recipe Finder"""
    
    # Modern color palette
    COLORS = {
        'primary': '#6366f1',      # Indigo
        'primary_dark': '#4f46e5',
        'primary_light': '#818cf8',
        'secondary': '#ec4899',    # Pink
        'success': '#10b981',      # Green
        'warning': '#f59e0b',      # Amber
        'danger': '#ef4444',       # Red
        'bg_main': '#f8fafc',      # Light gray-blue
        'bg_card': '#ffffff',
        'bg_hover': '#f1f5f9',
        'text_primary': '#1e293b',
        'text_secondary': '#64748b',
        'text_muted': '#94a3b8',
        'border': '#e2e8f0',
        'border_focus': '#6366f1',
        'shadow': '#00000008'
    }
    
    # Spacing constants for consistent layout
    SPACING = {
        'main_padding': 10,        # Main window padding
        'card_padding_x': 15,      # Card horizontal padding
        'card_padding_y': 12,      # Card vertical padding
        'element_gap': 8,          # Gap between elements
        'section_gap': 6           # Gap between sections
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("🍳 Recipe Finder - Modern Edition")
        self.root.geometry("1300x900")
        self.root.minsize(1100, 750)
        
        # Configure window background
        self.root.configure(bg=self.COLORS['bg_main'])
        
        # Store search results
        self.last_results: List[Recipe] = []
        self.selected_recipe: Optional[Recipe] = None
        
        # Configure modern styles
        self.setup_modern_styles()
        
        # Create GUI components
        self.create_widgets()
        
        # Center window
        self.center_window()
    
    def setup_modern_styles(self):
        """Setup modern, aesthetic ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main background
        style.configure('.', background=self.COLORS['bg_main'])
        
        # Title - Large, bold, modern
        style.configure(
            'Title.TLabel',
            font=('Segoe UI', 24, 'bold'),
            foreground=self.COLORS['text_primary'],
            background=self.COLORS['bg_main']
        )
        
        # Subtitle
        style.configure(
            'Subtitle.TLabel',
            font=('Segoe UI', 10),
            foreground=self.COLORS['text_secondary'],
            background=self.COLORS['bg_main']
        )
        
        # Card frames (white background with shadow effect)
        style.configure(
            'Card.TFrame',
            background=self.COLORS['bg_card'],
            relief='flat',
            borderwidth=0
        )
        
        # Modern LabelFrame
        style.configure(
            'Modern.TLabelframe',
            background=self.COLORS['bg_card'],
            relief='flat',
            borderwidth=0
        )
        style.configure(
            'Modern.TLabelframe.Label',
            font=('Segoe UI', 11, 'bold'),
            foreground=self.COLORS['text_primary'],
            background=self.COLORS['bg_card']
        )
        
        # Primary button (Indigo)
        style.configure(
            'Primary.TButton',
            font=('Segoe UI', 10, 'bold'),
            background=self.COLORS['primary'],
            foreground='white',
            borderwidth=0,
            focuscolor='none',
            relief='flat',
            padding=(20, 12)
        )
        style.map(
            'Primary.TButton',
            background=[('active', self.COLORS['primary_dark'])]
        )
        
        # Secondary button
        style.configure(
            'Secondary.TButton',
            font=('Segoe UI', 9),
            background=self.COLORS['bg_hover'],
            foreground=self.COLORS['text_primary'],
            borderwidth=1,
            relief='flat',
            padding=(14, 8)
        )
        style.map(
            'Secondary.TButton',
            background=[('active', self.COLORS['border'])]
        )
        
        # Modern Entry
        style.configure(
            'Modern.TEntry',
            fieldbackground='white',
            background='white',
            foreground=self.COLORS['text_primary'],
            borderwidth=2,
            relief='flat',
            padding=10
        )
        
        # Modern Combobox
        style.configure(
            'Modern.TCombobox',
            fieldbackground='white',
            background='white',
            foreground=self.COLORS['text_primary'],
            borderwidth=1,
            relief='flat',
            padding=8
        )
        
        # Treeview modern style
        style.configure(
            'Modern.Treeview',
            background='white',
            foreground=self.COLORS['text_primary'],
            fieldbackground='white',
            borderwidth=0,
            relief='flat',
            rowheight=35,
            font=('Segoe UI', 9)
        )
        style.configure(
            'Modern.Treeview.Heading',
            font=('Segoe UI', 10, 'bold'),
            background=self.COLORS['bg_hover'],
            foreground=self.COLORS['text_primary'],
            borderwidth=0,
            relief='flat'
        )
        style.map(
            'Modern.Treeview',
            background=[('selected', self.COLORS['primary_light'])],
            foreground=[('selected', 'white')]
        )
    
    def center_window(self):
        """Center the window on screen with error handling"""
        try:
            self.root.update_idletasks()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            x = (self.root.winfo_screenwidth() // 2) - (width // 2)
            y = (self.root.winfo_screenheight() // 2) - (height // 2)
            self.root.geometry(f'{width}x{height}+{x}+{y}')
        except Exception as e:
            # If centering fails, just use default position
            print(f"Warning: Could not center window: {e}")
    
    def create_widgets(self):
        """Create all modern GUI widgets - PROPERLY BALANCED"""
        
        # Main container with minimal padding
        main_frame = tk.Frame(self.root, bg=self.COLORS['bg_main'])
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=8)
        
        # Configure grid weights - DYNAMIC layout
        # Rows 0-2: Fixed height (header, search, filters)
        # Row 3 (results): weight=1 initially (full space when no selection)
        # Row 4 (details): weight=0 initially (hidden until recipe selected)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)  # Results
        main_frame.rowconfigure(4, weight=0)  # Details - initially hidden
        
        # Compact header section
        header_frame = tk.Frame(main_frame, bg=self.COLORS['bg_main'])
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 8))
        
        # Compact title with icon
        title = tk.Label(
            header_frame,
            text="🍳 Recipe Finder",
            font=('Segoe UI', 16, 'bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['bg_main']
        )
        title.pack(side=tk.LEFT)
        
        # Recipe count badge (compact) - dynamically counted
        total_recipes = len(FALLBACK_RECIPES)
        self.recipe_count_label = tk.Label(
            header_frame,
            text=f"{total_recipes} recipes",
            font=('Segoe UI', 8, 'bold'),
            bg=self.COLORS['primary'],
            fg='white',
            padx=8,
            pady=3
        )
        self.recipe_count_label.pack(side=tk.RIGHT)
        
        # Compact search section
        self.create_modern_search_section(main_frame)
        
        # Compact filters section (no card, just horizontal bar)
        self.create_compact_filters_section(main_frame)
        
        # MAXIMIZED Results section
        self.create_modern_results_section(main_frame)
        
        # Compact Details section (side-by-side with action buttons)
        self.create_compact_details_and_actions(main_frame)
    
    def _add_rounded_effect(self, widget):
        """Add visual rounded corner effect (simulated)"""
        # Note: True rounded corners require custom drawing
        # This adds some padding for a softer look
        widget.configure(relief='flat', bd=0)
    
    def create_modern_search_section(self, parent):
        """Create the modern search input section - COMPACT"""
        # Minimal card with less padding
        search_card = tk.Frame(parent, bg=self.COLORS['bg_card'], relief='flat', bd=0)
        search_card.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 6))
        self._add_card_shadow(search_card)
        
        # Inner padding frame - reduced padding
        search_frame = tk.Frame(search_card, bg=self.COLORS['bg_card'])
        search_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=12)
        search_frame.columnconfigure(1, weight=1)  # Make input column expand
        
        # Compact label and input on same row
        tk.Label(
            search_frame,
            text="🔍 Ingredients:",
            font=('Segoe UI', 9, 'bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['bg_card']
        ).grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        
        # Compact search input on same row
        entry_frame = tk.Frame(search_frame, bg='white', highlightthickness=1, 
                              highlightbackground=self.COLORS['border'])
        entry_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 8))
        
        self.ingredients_entry = tk.Entry(
            entry_frame,
            font=('Segoe UI', 10),
            fg=self.COLORS['text_primary'],
            bg='white',
            relief='flat',
            bd=0
        )
        self.ingredients_entry.pack(fill=tk.BOTH, padx=10, pady=6)
        self.ingredients_entry.insert(0, "chicken, tomato, onion, garlic")
        
        # Compact search button on same row
        self.search_btn = tk.Button(
            search_frame,
            text="🔍 Search",
            font=('Segoe UI', 9, 'bold'),
            bg=self.COLORS['primary'],
            fg='white',
            activebackground=self.COLORS['primary_dark'],
            activeforeground='white',
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.search_recipes,
            padx=20,
            pady=6
        )
        self.search_btn.grid(row=0, column=2)
        
        # Bind Enter key to search
        self.ingredients_entry.bind('<Return>', lambda e: self.search_recipes())
        
        # Focus effect for entry
        def on_entry_focus_in(e):
            entry_frame.configure(highlightbackground=self.COLORS['border_focus'])
        def on_entry_focus_out(e):
            entry_frame.configure(highlightbackground=self.COLORS['border'])
        
        self.ingredients_entry.bind('<FocusIn>', on_entry_focus_in)
        self.ingredients_entry.bind('<FocusOut>', on_entry_focus_out)
    
    def _add_card_shadow(self, widget):
        """
        Add subtle shadow effect to card widget (visual enhancement).
        
        Args:
            widget: Tkinter widget to add shadow border to
        """
        try:
            widget.configure(highlightthickness=1, highlightbackground='#e2e8f0')
        except Exception as e:
            # If shadow fails, widget will still work without it
            print(f"Warning: Could not add shadow to widget: {e}")
    
    def create_compact_filters_section(self, parent):
        """Create COMPACT filters section - no card, just horizontal bar"""
        # Simple horizontal frame - NO CARD, minimal padding
        filters_frame = tk.Frame(parent, bg=self.COLORS['bg_hover'])
        filters_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 6))
        
        # Inner frame with minimal padding
        inner = tk.Frame(filters_frame, bg=self.COLORS['bg_hover'])
        inner.pack(fill=tk.X, padx=15, pady=6)
        
        # All filters in ONE ROW - compact labels
        tk.Label(inner, text="Provider:", font=('Segoe UI', 8), 
                fg=self.COLORS['text_secondary'], bg=self.COLORS['bg_hover']).pack(side=tk.LEFT, padx=(0, 4))
        
        self.provider_var = tk.StringVar(value="fast")
        ttk.Combobox(inner, textvariable=self.provider_var,
                    values=["fast", "tasty", "edamam"], state="readonly",
                    width=10, font=('Segoe UI', 8)).pack(side=tk.LEFT, padx=(0, 15))
        
        tk.Label(inner, text="Results:", font=('Segoe UI', 8),
                fg=self.COLORS['text_secondary'], bg=self.COLORS['bg_hover']).pack(side=tk.LEFT, padx=(0, 4))
        
        self.max_results_var = tk.StringVar(value="20")
        ttk.Spinbox(inner, from_=5, to=50, textvariable=self.max_results_var,
                   width=5, font=('Segoe UI', 8)).pack(side=tk.LEFT, padx=(0, 15))
        
        tk.Label(inner, text="Diet:", font=('Segoe UI', 8),
                fg=self.COLORS['text_secondary'], bg=self.COLORS['bg_hover']).pack(side=tk.LEFT, padx=(0, 4))
        
        self.diet_var = tk.StringVar(value="")
        ttk.Combobox(inner, textvariable=self.diet_var,
                    values=["", "vegetarian", "vegan", "gluten-free"],
                    state="readonly", width=12, font=('Segoe UI', 8)).pack(side=tk.LEFT, padx=(0, 15))
        
        tk.Label(inner, text="Max Time:", font=('Segoe UI', 8),
                fg=self.COLORS['text_secondary'], bg=self.COLORS['bg_hover']).pack(side=tk.LEFT, padx=(0, 4))
        
        self.max_time_var = tk.StringVar(value="")
        tk.Entry(inner, textvariable=self.max_time_var, width=5,
                font=('Segoe UI', 8), bg='white').pack(side=tk.LEFT, padx=(0, 15))
        
        tk.Label(inner, text="Sort:", font=('Segoe UI', 8),
                fg=self.COLORS['text_secondary'], bg=self.COLORS['bg_hover']).pack(side=tk.LEFT, padx=(0, 4))
        
        self.sort_var = tk.StringVar(value="match")
        ttk.Combobox(inner, textvariable=self.sort_var,
                    values=["match", "time-asc", "time-desc"],
                    state="readonly", width=10, font=('Segoe UI', 8)).pack(side=tk.LEFT)
    
    def create_modern_results_section(self, parent):
        """Create MAXIMIZED results section"""
        # Minimal card with less padding
        results_card = tk.Frame(parent, bg=self.COLORS['bg_card'], relief='flat', bd=0)
        results_card.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 6))
        self._add_card_shadow(results_card)
        
        # Minimal padding frame
        results_frame = tk.Frame(results_card, bg=self.COLORS['bg_card'])
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)
        
        # Compact header
        header = tk.Label(
            results_frame,
            text="📋 Results",
            font=('Segoe UI', 9, 'bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['bg_card']
        )
        header.grid(row=0, column=0, sticky=tk.W, pady=(0, 6))
        
        # Create modern Treeview for results
        tree_frame = tk.Frame(results_frame, bg='white', highlightthickness=1,
                             highlightbackground=self.COLORS['border'])
        tree_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        columns = ("match", "have", "need", "time", "provider")
        self.results_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="tree headings",
            selectmode="browse",
            style='Modern.Treeview'
        )
        
        # Configure columns with icons
        self.results_tree.heading("#0", text="📖 Recipe Title")
        self.results_tree.heading("match", text="✨ Match")
        self.results_tree.heading("have", text="✓ Have")
        self.results_tree.heading("need", text="+ Need")
        self.results_tree.heading("time", text="⏱️ Time")
        self.results_tree.heading("provider", text="📍 Source")
        
        self.results_tree.column("#0", width=350)
        self.results_tree.column("match", width=90, anchor=tk.CENTER)
        self.results_tree.column("have", width=90, anchor=tk.CENTER)
        self.results_tree.column("need", width=90, anchor=tk.CENTER)
        self.results_tree.column("time", width=90, anchor=tk.CENTER)
        self.results_tree.column("provider", width=120)
        
        # Modern scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid layout
        self.results_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind selection event
        self.results_tree.bind('<<TreeviewSelect>>', self.on_recipe_select)
        
        # Add alternating row colors
        self.results_tree.tag_configure('oddrow', background='#f8fafc')
        self.results_tree.tag_configure('evenrow', background='white')
    
    def create_compact_details_and_actions(self, parent):
        """Create combined details and action buttons - DYNAMIC display"""
        # Card frame that expands vertically
        self.details_card = tk.Frame(parent, bg=self.COLORS['bg_card'], relief='flat', bd=0)
        self.details_card.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 8))
        self._add_card_shadow(self.details_card)
        # Initially hide the details section
        self.details_card.grid_remove()
        self.details_visible = False
        
        # Inner frame to hold details + buttons
        combined_frame = tk.Frame(self.details_card, bg=self.COLORS['bg_card'])
        combined_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=12)
        
        # Left side - Details section (75% width)
        details_container = tk.Frame(combined_frame, bg=self.COLORS['bg_card'])
        details_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 12))
        
        # Section header
        tk.Label(
            details_container,
            text="📝 Recipe Details",
            font=('Segoe UI', 10, 'bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['bg_card']
        ).pack(anchor=tk.W, pady=(0, 8))
        
        # Details text with border for visibility
        text_frame = tk.Frame(details_container, bg='white', 
                             highlightthickness=1, highlightbackground=self.COLORS['border'])
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrolled text that will expand to fill available space
        self.details_text = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 9),
            bg='white',
            fg=self.COLORS['text_primary'],
            relief='flat',
            bd=0,
            padx=12,
            pady=10
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        self.details_text.insert(1.0, "Select a recipe from the results above to view detailed information...\n\nIngredients, instructions, cooking time, and more will appear here.")
        self.details_text.configure(state='disabled')
    
        
        # Right side - Action buttons (25% width, fixed)
        buttons_container = tk.Frame(combined_frame, bg=self.COLORS['bg_card'], width=180)
        buttons_container.pack(side=tk.RIGHT, fill=tk.Y)
        buttons_container.pack_propagate(False)  # Maintain fixed width
        
        # Section header
        tk.Label(
            buttons_container,
            text="Actions",
            font=('Segoe UI', 10, 'bold'),
            fg=self.COLORS['text_primary'],
            bg=self.COLORS['bg_card']
        ).pack(anchor=tk.W, pady=(0, 8))
        
        # Export button
        self.export_btn = tk.Button(
            buttons_container,
            text="📁 Export",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_hover'],
            fg=self.COLORS['text_primary'],
            activebackground=self.COLORS['border'],
            activeforeground=self.COLORS['text_primary'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.export_results,
            state='disabled',
            pady=10
        )
        self.export_btn.pack(fill=tk.X, pady=(0, 6))
        
        # View recipe button
        self.view_btn = tk.Button(
            buttons_container,
            text="🔗 View Online",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_hover'],
            fg=self.COLORS['text_primary'],
            activebackground=self.COLORS['border'],
            activeforeground=self.COLORS['text_primary'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.view_recipe_online,
            state='disabled',
            pady=10
        )
        self.view_btn.pack(fill=tk.X, pady=(0, 6))
        
        # Clear button
        clear_btn = tk.Button(
            buttons_container,
            text="🗑️ Clear",
            font=('Segoe UI', 9),
            bg=self.COLORS['bg_hover'],
            fg=self.COLORS['text_primary'],
            activebackground=self.COLORS['border'],
            activeforeground=self.COLORS['text_primary'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.clear_results,
            pady=10
        )
        clear_btn.pack(fill=tk.X, pady=(0, 12))
        
        # Status label below buttons
        self.status_label = tk.Label(
            buttons_container,
            text="Ready to search",
            font=('Segoe UI', 9),
            fg=self.COLORS['text_muted'],
            bg=self.COLORS['bg_card'],
            pady=10,
            wraplength=160,
            justify=tk.LEFT
        )
        self.status_label.pack(fill=tk.X)
    
    def search_recipes(self):
        """
        Search for recipes based on user input from GUI fields.
        
        Collects all filter parameters, validates inputs, performs search,
        and displays results. Handles errors gracefully and provides user feedback.
        """
        # Get inputs
        ingredients_str = self.ingredients_entry.get().strip()
        if not ingredients_str:
            messagebox.showwarning("Input Required", "Please enter some ingredients!")
            return
        
        provider = self.provider_var.get()
        max_results = int(self.max_results_var.get())
        diet = self.diet_var.get() if self.diet_var.get() else None
        sort_by = self.sort_var.get()
        
        max_minutes = None
        if self.max_time_var.get():
            try:
                max_minutes = int(self.max_time_var.get())
            except ValueError:
                pass
        
        # Hide details section when starting new search
        self.hide_details_section()
        
        # Update status with modern styling
        self.status_label.config(text="🔍 Searching...", fg=self.COLORS['primary'], bg=self.COLORS['bg_main'])
        self.root.update()
        
        # Disable search button
        self.search_btn.config(state='disabled')
        
        try:
            # Search recipes
            self.last_results = search_recipes(
                ingredients_str=ingredients_str,
                provider=provider,
                max_results=max_results,
                diet=diet,
                max_minutes=max_minutes,
                sort_by=sort_by
            )
            
            # Display results
            self.display_results()
            
            # Update status with modern colors
            if self.last_results:
                self.status_label.config(
                    text=f"✅ Found {len(self.last_results)} recipes",
                    fg=self.COLORS['success'],
                    bg=self.COLORS['bg_main']
                )
                self.export_btn.config(state='normal')
            else:
                self.status_label.config(
                    text="⚠️ No recipes found",
                    fg=self.COLORS['warning'],
                    bg=self.COLORS['bg_main']
                )
                messagebox.showinfo(
                    "No Results",
                    "No recipes found matching your criteria.\n\nTry:\n"
                    "• Fewer ingredients\n"
                    "• Different provider\n"
                    "• Removing filters"
                )
        
        except Exception as e:
            self.status_label.config(
                text="❌ Error",
                fg=self.COLORS['danger'],
                bg=self.COLORS['bg_main']
            )
            messagebox.showerror("Error", f"Search failed:\n{str(e)}")
        
        finally:
            # Re-enable search button
            self.search_btn.config(state='normal')
    
    def display_results(self):
        """Display search results in the tree with modern styling"""
        # Clear existing items
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Add new items with alternating row colors
        for idx, recipe in enumerate(self.last_results):
            match = f"{recipe.match_percentage:.0f}%"
            have = str(len(recipe.used_ingredients))
            need = str(len(recipe.missing_ingredients))
            time = f"{recipe.ready_in_minutes}m" if recipe.ready_in_minutes else "-"
            
            # Alternate row colors
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            
            self.results_tree.insert(
                "",
                tk.END,
                text=f"  {recipe.title}",  # Add padding
                values=(match, have, need, time, recipe.provider.value),
                tags=(tag,)
            )
    
    def on_recipe_select(self, event):
        """Handle recipe selection - SHOW details section and scroll to keep item visible"""
        selection = self.results_tree.selection()
        if not selection:
            # No selection - hide details section
            self.hide_details_section()
            return
        
        # Get selected index
        item = selection[0]
        index = self.results_tree.index(item)
        
        if 0 <= index < len(self.last_results):
            self.selected_recipe = self.last_results[index]
            self.show_details_section()  # Show details section (50/50 split)
            self.display_recipe_details(self.selected_recipe)
            self.view_btn.config(state='normal' if self.selected_recipe.source_url else 'disabled')
            
            # Scroll selected item to top to prevent overlap with details section
            self.results_tree.see(item)
            # Additional scroll adjustment: try to position it near the top
            self._scroll_selected_to_top(item)
    
    def display_recipe_details(self, recipe: Recipe):
        """Display detailed information for a recipe"""
        self.details_text.configure(state='normal')
        self.details_text.delete(1.0, tk.END)
        
        # Build details text
        details = f"📖 {recipe.title}\n"
        details += "=" * 60 + "\n\n"
        
        # Meta info
        if recipe.cuisine or recipe.servings or recipe.ready_in_minutes:
            meta = []
            if recipe.cuisine:
                meta.append(f"🌍 {recipe.cuisine}")
            if recipe.servings:
                meta.append(f"🍽️ {recipe.servings} servings")
            if recipe.ready_in_minutes:
                meta.append(f"⏱️ {recipe.ready_in_minutes} min")
            details += " | ".join(meta) + "\n\n"
        
        # Match info
        details += f"Match: {recipe.match_percentage:.0f}% "
        details += f"({len(recipe.used_ingredients)} have / {len(recipe.missing_ingredients)} need)\n\n"
        
        # Ingredients you have
        if recipe.used_ingredients:
            details += "✓ Ingredients you have:\n"
            for ing in recipe.used_ingredients:
                details += f"  • {ing}\n"
            details += "\n"
        
        # Ingredients you need
        if recipe.missing_ingredients:
            details += "⚠ Ingredients you need:\n"
            for ing in recipe.missing_ingredients[:10]:  # Limit to 10
                details += f"  • {ing}\n"
            if len(recipe.missing_ingredients) > 10:
                details += f"  ... and {len(recipe.missing_ingredients) - 10} more\n"
            details += "\n"
        
        # Categories
        if recipe.category_or_diet:
            details += f"Tags: {', '.join(recipe.category_or_diet[:5])}\n\n"
        
        # Source link
        if recipe.source_url:
            details += f"🔗 Recipe URL: {recipe.source_url}\n"
        
        self.details_text.insert(1.0, details)
        self.details_text.configure(state='disabled')
    
    def show_details_section(self):
        """
        Show the details section and reconfigure layout to 50/50 split.
        
        When a recipe is selected, this method:
        - Makes the hidden details card visible
        - Adjusts grid weights so results and details each take 50% of space
        - Forces a layout refresh for immediate visual update
        """
        if not self.details_visible:
            # Get the main frame (parent of details_card)
            main_frame = self.details_card.master
            # Reconfigure weights for 50/50 split
            main_frame.rowconfigure(3, weight=1)  # Results - 50%
            main_frame.rowconfigure(4, weight=1)  # Details - 50%
            # Show the details section
            self.details_card.grid()
            self.details_visible = True
            # Force layout update
            self.root.update_idletasks()
    
    def _scroll_selected_to_top(self, item):
        """
        Scroll the selected item to a visible position in the results section.
        
        This prevents the details section from covering the selected item
        when it appears at the bottom half of the results list.
        
        Strategy: Position the selected item in the top quarter of visible area
        so it remains visible when the details section takes the bottom 50%.
        
        Args:
            item: Treeview item identifier to scroll into view
        """
        try:
            # Get the index of the selected item
            index = self.results_tree.index(item)
            # Get all items
            children = self.results_tree.get_children()
            total_items = len(children)
            
            if total_items == 0:
                return
            
            # Calculate position: try to place selected item at 20% from top
            # This ensures it's visible in the top 50% when details appear
            target_position = max(0, (index - 2) / total_items)  # Show 2-3 items above selected
            
            # Apply scroll
            self.results_tree.yview_moveto(target_position)
            
            # Small delay to ensure layout is stable, then scroll again
            self.root.after(50, lambda: self.results_tree.see(item))
            
        except Exception as e:
            # If scrolling fails, at least the see() call will make it visible
            print(f"Warning: Could not optimize scroll position: {e}")
    
    def hide_details_section(self):
        """
        Hide the details section and give full space back to results.
        
        When no recipe is selected or a new search is performed:
        - Hides the details card
        - Adjusts grid weights to give results 100% of space
        - Clears the current recipe selection
        - Disables the "View Online" button
        - Forces a layout refresh
        """
        if self.details_visible:
            # Get the main frame
            main_frame = self.details_card.master
            # Give full space back to results
            main_frame.rowconfigure(3, weight=1)  # Results - 100%
            main_frame.rowconfigure(4, weight=0)  # Details - hidden
            # Hide the details section
            self.details_card.grid_remove()
            self.details_visible = False
            # Clear selection
            self.selected_recipe = None
            self.view_btn.config(state='disabled')
            # Force layout update
            self.root.update_idletasks()
    
    def view_recipe_online(self):
        """Open recipe in web browser"""
        if self.selected_recipe and self.selected_recipe.source_url:
            webbrowser.open(self.selected_recipe.source_url)
    
    def export_results(self):
        """Export search results"""
        if not self.last_results:
            messagebox.showwarning("No Results", "No results to export!")
            return
        
        # Ask for file path
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[
                ("JSON files", "*.json"),
                ("CSV files", "*.csv"),
                ("HTML files", "*.html"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                export_recipes(self.last_results, file_path)
                messagebox.showinfo(
                    "Export Successful",
                    f"Exported {len(self.last_results)} recipes to:\n{file_path}"
                )
            except Exception as e:
                messagebox.showerror("Export Failed", f"Failed to export:\n{str(e)}")
    
    def clear_results(self):
        """Clear all results"""
        # Clear tree
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Clear details
        self.details_text.configure(state='normal')
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(1.0, "Select a recipe to view details...")
        self.details_text.configure(state='disabled')
        
        # Clear results
        self.last_results = []
        self.selected_recipe = None
        
        # Disable buttons
        self.export_btn.config(state='disabled')
        self.view_btn.config(state='disabled')
        
        # Update status with modern colors
        self.status_label.config(
            text="Ready to search",
            fg=self.COLORS['text_muted'],
            bg=self.COLORS['bg_main']
        )


def main():
    """Main entry point for modern GUI"""
    root = tk.Tk()
    app = ModernRecipeFinderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

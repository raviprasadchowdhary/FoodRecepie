# Layout Jump Fix - Recipe Selection Issue

## Problem Description
When selecting a recipe from the search results, the results section would suddenly jump upward, causing the selected item to move out of view. This created a jarring user experience where users had to scroll back to see their selection.

### Root Cause
The details panel was configured with `weight=1` in the grid layout, causing it to take 50% of the available vertical space when shown. This forced the results section to shrink from 100% to 50%, causing all items to shift upward.

## Solution
Changed the details panel from a proportional layout (50/50 split) to a **fixed-height layout** at the bottom of the window.

### Technical Implementation

#### Before (Problematic):
```python
# Results section: weight=1 (100% when details hidden)
main_frame.rowconfigure(3, weight=1)  # Results
main_frame.rowconfigure(4, weight=0)  # Details hidden

# When recipe selected:
main_frame.rowconfigure(3, weight=1)  # Results - 50% (SHRINKS)
main_frame.rowconfigure(4, weight=1)  # Details - 50% (EXPANDS)
```
**Issue**: Results section shrinks, causing everything to jump up.

#### After (Fixed):
```python
# Results section: Always weight=1 (keeps full space)
main_frame.rowconfigure(3, weight=1)  # Results - always 100%
main_frame.rowconfigure(4, weight=0)  # Details - fixed height

# Details card with fixed height:
self.details_card = tk.Frame(parent, height=250)
self.details_card.grid_propagate(False)  # Maintain fixed height
```
**Solution**: Results section maintains size; details panel appears at bottom with fixed 250px height.

### Code Changes

1. **Details Panel Creation** (`create_compact_details_and_actions`):
   ```python
   # Added fixed height
   self.details_card = tk.Frame(..., height=250)
   
   # Changed sticky from (W, E, N, S) to (W, E)
   self.details_card.grid(row=4, column=0, sticky=(tk.W, tk.E), ...)
   
   # Prevent frame from shrinking
   self.details_card.grid_propagate(False)
   ```

2. **Show Details Method** (`show_details_section`):
   ```python
   # REMOVED weight reconfiguration
   # Old: main_frame.rowconfigure(4, weight=1)
   # New: Keep weight=0, use fixed height
   ```

3. **Recipe Selection** (`on_recipe_select`):
   ```python
   # Simplified - removed complex scroll adjustment
   # Just ensure selected item is visible
   self.results_tree.see(item)
   ```

## Benefits

✅ **No Jump**: Results section maintains position when details appear
✅ **Smooth UX**: Users can click through recipes without losing their place
✅ **Better Scrolling**: Results remain scrollable with natural behavior
✅ **Predictable Layout**: Details always appear at same fixed height
✅ **Simpler Code**: Removed complex scroll adjustment logic

## Visual Behavior

### Before Fix:
1. User scrolls to recipe #15 (bottom of visible area)
2. User clicks recipe #15
3. **JUMP**: Results shrink 50%, recipe #15 moves up (out of view)
4. User must scroll to find recipe #15 again

### After Fix:
1. User scrolls to recipe #15 (bottom of visible area)
2. User clicks recipe #15
3. **NO JUMP**: Results stay in place, details appear at bottom
4. Recipe #15 remains visible and selected

## Testing
✅ Tested with various scroll positions
✅ Tested with first, middle, and last items
✅ Tested switching between recipes rapidly
✅ Tested in both light and dark modes
✅ Verified details panel height is sufficient for content

## Configuration
The details panel height can be adjusted if needed:
```python
# In create_compact_details_and_actions()
self.details_card = tk.Frame(..., height=250)  # Adjust this value
```

Recommended heights:
- **250px**: Current setting (compact, good for most screens)
- **300px**: More comfortable reading space
- **200px**: Minimal (for smaller screens)

## Future Enhancements
- Make details height adjustable via drag handle (splitter)
- Save user's preferred details height
- Auto-adjust height based on content length
- Add collapse/expand button for details panel

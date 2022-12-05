import game
import gui

grid, empty_cells = game.generate_grid()
width = gui.get_cell_width()
print(gui.get_display_grid(grid, width))
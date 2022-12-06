import game
import gui

grid, empty_cells = game.generate_grid()
width = gui.get_cell_width()

gui.clear()
while True:
    gui.display_grid(grid, width, clear_console=True)
    move_key = gui.get_move()
    if not move_key in game.CONTROLS: continue
    move = game.CONTROLS[move_key]
    game.make_move(move, grid)
    if move == game.MOVE_EXIT: break
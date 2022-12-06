import game
import gui
import config

grid = game.generate_grid()
width = gui.get_cell_width()

gui.clear()
while True:
    gui.display_grid(grid, width, clear_console=True)
    move_key = gui.get_move()
    if not move_key in config.CONTROLS: continue
    move = config.CONTROLS[move_key]
    if game.make_move(move, grid):
        game.add_val(grid, 2)
    if move == config.MOVE_EXIT: break
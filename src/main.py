import game
import gui
import config

def play() -> None:
    grid = game.generate_grid()
    config.CELL_WIDTH = gui.get_cell_width()
    score = 0

    while True:
        gui.clear()
        gui.display_grid(grid)
        gui.display_score(score)
        move_key = gui.get_move()
        if not move_key in config.CONTROLS: continue
        move = config.CONTROLS[move_key]
        was_moved, points = game.make_move(move, grid)
        score += points
        if was_moved:
            game.add_random_val(grid)


if __name__ == '__main__':
    play()
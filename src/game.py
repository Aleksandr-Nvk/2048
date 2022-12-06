import random
import gui
import config


def add_val(grid:list, val:int) -> None:
    if val < 2 or val.bit_count() != 1:
        raise ValueError(f"Parameter 'val' must equal 2^x, where x >= 1. Received: {val}.")
    
    empty_cells = [(x, y) for x in range(config.GRID_DIM) for y in range(config.GRID_DIM) if not grid[x][y]]
    cell = empty_cells.pop(random.randrange(len(empty_cells)))
    grid[cell[0]][cell[1]] = val


def generate_grid() -> list:
    grid = [[0] * config.GRID_DIM for _ in range(config.GRID_DIM)]
    add_val(grid, 2)
    add_val(grid, 2)
    return grid


def move_right(grid:list) -> None:
    was_moved = False
    for i, row in enumerate(grid):
        init_row = row.copy()
        values = list(filter(bool, row))
        cur = len(values) - 1
        nxt = cur - 1
        while nxt >= 0:
            if values[cur] == values[nxt]:
                values[cur] *= 2
                values[nxt] = 0
                cur -= 1
                nxt -= 1
            cur -= 1
            nxt -= 1
        
        values = list(filter(bool, values))
        row.clear()
        row.extend([0] * (config.GRID_DIM - len(values)) + values)
        was_moved |= init_row != row

    return was_moved


def move_left(grid:list) -> None:
    pass


def move_up(grid:list) -> None:
    pass


def move_down(grid:list) -> None:
    pass


def make_move(move:str, grid:list) -> None:
    if move == config.MOVE_EXIT:
        gui.exit_game()
        return False
    elif move == config.MOVE_RIGHT:
        return move_right(grid)
    elif move == config.MOVE_LEFT:
        return move_left(grid)
    elif move == config.MOVE_UP:
        return move_up(grid)
    elif move == config.MOVE_DOWN:
        return move_down(grid)
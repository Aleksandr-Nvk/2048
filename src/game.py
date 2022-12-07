import gui
import config
import random


def add_val(grid:list, val:int) -> None:
    if val < 2 or val.bit_count() != 1:
        raise ValueError(f"Parameter 'val' must equal 2^x, where x >= 1. Received: {val}.")
    
    empty_cells = [(x, y) for x in range(config.GRID_DIM) for y in range(config.GRID_DIM) if not grid[x][y]]
    cell = empty_cells.pop(random.randrange(len(empty_cells)))
    grid[cell[0]][cell[1]] = val


def add_random_val(grid:list) -> None:
    add_val(grid, random.choice([2] * 15 + [4]))


def generate_grid() -> list:
    grid = [[0] * config.GRID_DIM for _ in range(config.GRID_DIM)]
    add_val(grid, 2)
    add_val(grid, 2)
    return grid


def validate_magnitude(magnitude:int) -> None:
    if magnitude not in (-1, +1):
        raise ValueError(f"Parameter 'magnitude' must be either -1 or +1. Received: {magnitude}.")


def reduce(values:list, magnitude:int) -> tuple:
    validate_magnitude(magnitude)

    start = (len(values) - 1) if magnitude == +1 else 0
    next = (start - 1) if magnitude == +1 else 1
    points = 0
    while (next >= 0) if magnitude == +1 else (next < len(values)) :
        if values[start] == values[next]:
            values[start] *= 2
            values[next] = 0
            points += values[start]
            start -= magnitude
            next -= magnitude

        start -= magnitude
        next -= magnitude

    values = list(filter(bool, values))
    return values, points


def move_horizontally(grid:list, magnitude:int) -> tuple:
    validate_magnitude(magnitude)

    was_moved = False
    points = 0
    for row in grid:
        init_row = row.copy()
        values, points_row = reduce(list(filter(bool, row)), magnitude)
        points += points_row
        row.clear()
        zeros = [0] * (config.GRID_DIM - len(values))
        row.extend((zeros + values) if magnitude == +1 else (values + zeros))
        was_moved |= init_row != row

    return was_moved, points


def move_vertically(grid:list, magnitude:int) -> tuple:
    validate_magnitude(magnitude)

    was_moved = False
    points = 0
    columns_indexes = [[(y, x) for y in range(config.GRID_DIM)] for x in range(config.GRID_DIM)]
    for column_indexes in columns_indexes:
        col = list(map(lambda x: grid[x[0]][x[1]], column_indexes))
        init_col = col.copy()
        values, points_column = reduce(list(filter(bool, col)), magnitude)
        points += points_column        
        col.clear()
        zeros = [0] * (config.GRID_DIM - len(values))
        col.extend((zeros + values) if magnitude == +1 else (values + zeros))
        for i, column_index in enumerate(column_indexes):
            grid[column_index[0]][column_index[1]] = col[i]
            
        was_moved |= init_col != col

    return was_moved, points


def make_move(move:str, grid:list) -> tuple:
    if move == config.MOVE_EXIT:
        gui.exit_game()
        result = False, 0
    elif move == config.MOVE_RIGHT:
        result = move_horizontally(grid, +1)
    elif move == config.MOVE_LEFT:
        result = move_horizontally(grid, -1)
    elif move == config.MOVE_UP:
        result = move_vertically(grid, -1)
    elif move == config.MOVE_DOWN:
        result = move_vertically(grid, +1)
    else:
        result = False, 0
    
    if [x for row in grid for x in row if x == config.MAX_VAL]:
        gui.win(grid)

    return result
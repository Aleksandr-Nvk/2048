import random

GRID_DIM = 4 # dimension of the grid. 4x4 in the original version of 2048
MAX_VAL = 2048 # value which indicates victory. 2048 in the original version of 2048
MAX_VAL_STR = str(MAX_VAL)
MAX_VAL_LEN = len(MAX_VAL_STR)

def add_val(grid:list, empty_cells:list, val:int) -> None:
    if val < 2 or val.bit_count() != 1:
        raise ValueError(f"Parameter 'val' must equal 2^x, where x >= 1. Received: {val}.")
    
    cell = empty_cells.pop(random.randrange(len(empty_cells)))
    grid[cell[0]][cell[1]] = val

def generate_grid() -> tuple:
    grid = [[None] * GRID_DIM for _ in range(GRID_DIM)]
    empty_cells = [(x, y) for x in range(GRID_DIM) for y in range(GRID_DIM)]
    add_val(grid, empty_cells, 2)
    add_val(grid, empty_cells, 2)

    return grid, empty_cells
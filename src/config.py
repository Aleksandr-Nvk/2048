GRID_DIM = 4 # dimension of the grid. 4x4 in the original version of 2048
MAX_VAL = 2048 # value which indicates victory. 2048 in the original version of 2048

CELL_WIDTH = 8

MOVE_UP = 'up'
MOVE_DOWN = 'down'
MOVE_LEFT = 'left'
MOVE_RIGHT = 'right'
MOVE_EXIT = 'exit'

EXPAND_CELL = 'd'
SHRINK_CELL = 'a'
SAVE_CELL = 's'

CONTROLS = {
    'w': MOVE_UP,
    's': MOVE_DOWN,
    'a': MOVE_LEFT,
    'd': MOVE_RIGHT,
    'x': MOVE_EXIT,
}
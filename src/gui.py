import config
import os

MAX_VAL_STR = str(config.MAX_VAL)
MAX_VAL_LEN = len(MAX_VAL_STR)


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


def display_cell(width:int) -> str:
    if width < MAX_VAL_LEN:
        raise ValueError(f"Parameter 'width' must greater or equal to 'MAX_VAL_LEN'. Received: {width}.")
    
    line = ('-' * MAX_VAL_LEN).center(width, '-')
    space = (' ' * MAX_VAL_LEN).center(width)
    value = MAX_VAL_STR.center(width)
    print(f"""\
+{line}+
|{space}|
|{value}|
|{space}|
+{line}+""")


def get_cell_width() -> int:
    width = 10
    while True:
        clear()
        display_cell(width)
        val_raw = input("Make sure you are running your terminal window in decent dimensions (switch to fullscreen mode if needed).\
Use keys 'd' ('D') and 'a' ('A') on your keyboard to increase or decrese the width of a single cell.\
The cell must look like as close to a square as possible.\nEnter 's' ('S') when you are done:")
        val_raw = val_raw.lower()
        if val_raw == config.SHRINK_CELL and width > MAX_VAL_LEN:
            width -= 1
        elif val_raw == config.EXPAND_CELL:
            width += 1
        elif val_raw == config.SAVE_CELL:
            break
    
    return width


def display_grid(grid:list, cell_width:int=config.CELL_WIDTH) -> None:
    line = f"+{'+'.join([('-' * cell_width)] * config.GRID_DIM)}+"
    space = f"|{'|'.join([(' ' * cell_width)] * config.GRID_DIM)}|"
    lines = [line]
    for row in grid:
        lines.append(space)
        values_with_spaces = [str(x or ' ').center(cell_width) for x in row]
        content = f"|{'|'.join(values_with_spaces)}|"
        lines.append(content)
        lines.append(space)
        lines.append(line)

    print(*lines, sep='\n')


def get_move() -> str | None:
    val_raw = input(("Use 'WASD' ('wasd') keys to swipe up, left, down, and right respectively. " +
    "Enter 'x' ('X') to exit the game: ")).lower()
    if len(val_raw) == 1 and val_raw in config.CONTROLS:
        return val_raw


def display_score(score:int) -> None:
    print(f'SCORE: {score}')


def exit_game() -> None:
    print('\nBye...')
    exit()


def win(grid):
    clear()
    display_grid(grid)
    print('You won! ;-D')
    exit_game()
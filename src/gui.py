import os
import game

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def get_display_cell(width:int) -> str:
    if width < game.MAX_VAL_LEN:
        raise ValueError(f"Parameter 'width' must greater or equal to 'MAX_VAL_LEN'. Received: {width}.")
    
    line = ('-' * game.MAX_VAL_LEN).center(width, '-')
    space = (' ' * game.MAX_VAL_LEN).center(width)
    value = game.MAX_VAL_STR.center(width)
    return f"""\
+{line}+
|{space}|
|{value}|
|{space}|
+{line}+"""

def get_cell_width() -> int:
    width = 7
    while True:
        clear()
        print(get_display_cell(width))
        val_raw = input("Make sure you are running your terminal window in decent dimensions (switch to fullscreen mode if needed).\
Use keys 'd' ('D') and 'a' ('A') on your keyboard to increase or decrese the width of a single cell.\
The cell must look like as close to a square as possible.\nEnter 's' ('S') when you are done:")
        val_raw = val_raw.lower()
        if val_raw == 'a' and width > game.MAX_VAL_LEN:
            width -= 1
        elif val_raw == 'd':
            width += 1
        elif val_raw == 's':
            break
    
    return width

def get_display_grid(grid:list, cell_width:int) -> str:
    line = f"+{'+'.join([('-' * cell_width)] * game.MAX_VAL_LEN)}+"
    space = f"|{'|'.join([(' ' * cell_width)] * game.MAX_VAL_LEN)}|"
    lines = [line]
    for row in grid:
        lines.append(space)
        values_with_spaces = [str(x or ' ').center(cell_width) for x in row]
        content = f"|{'|'.join(values_with_spaces)}|"
        lines.append(content)
        lines.append(space)
        lines.append(line)

    return '\n'.join(lines)

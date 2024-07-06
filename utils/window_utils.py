def draw_window(stdscr, rows, cols, x, y):
    window = stdscr.subwin(rows, cols, y, x)
    window.immedok(True)
    window.box()
    window.border(0)
    window.refresh()
    return window

def clear_rectangle(win, start_x, start_y, end_x, end_y):
    """
    Clears a rectangle in the given window by setting the characters to spaces.
    
    :param win: The window object (curses window)
    :param start_x: The starting x-coordinate (column)
    :param start_y: The starting y-coordinate (row)
    :param end_x: The ending x-coordinate (column)
    :param end_y: The ending y-coordinate (row)
    """
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            win.addch(y, x, ' ')
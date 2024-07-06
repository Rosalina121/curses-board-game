def draw_window(stdscr, rows, cols, x, y):
    window = stdscr.subwin(rows, cols, y, x)
    window.immedok(True)
    window.box()
    window.border(0)
    window.refresh()
    return window
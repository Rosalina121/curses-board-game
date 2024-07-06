from . import window_utils

def draw_game(stdscr, rows, cols):
    game_window = window_utils.draw_window(stdscr, rows, cols, x=0, y=rows)

    game_window.addstr(0, 1, "┤Game: ???├")
    # game_window.addstr(1, 2, game)
    return game_window

def draw_new_game(game_window, game):
    game_window.erase()
    game_window.border(0)
    if game == "M":
        draw_milionerzy(game_window)
    elif game == "1":
        draw_1z10(game_window)
    elif game == "J":
        draw_jaka_to_melodia(game_window)


def draw_milionerzy(game_window):
    game_window.addstr(0, 1, "┤Game: Milionerzy├")

def draw_1z10(game_window):
    game_window.addstr(0, 1, "┤Game: 1 z 10├")

def draw_jaka_to_melodia(game_window):
    game_window.addstr(0, 1, "┤Game: Jaka to Melodia?├")
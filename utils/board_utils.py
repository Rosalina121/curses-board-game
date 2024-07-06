from . import window_utils

def draw_board(stdscr, rows, cols, board_width):
    board_window = window_utils.draw_window(stdscr, rows, board_width, x=0, y=0)

    board_window.addstr(15, 5, f"{rows}x{cols-22}")
    board_window.addstr(0, 1, "┤Teleturnieje Planszówka├")

    return board_window

def draw_board_play(board_array, board_window):
    for i in range(27):
        board_window.addstr(3 + 4, (i * 2) + 2, board_array[i].game)

def draw_board_players(players, board_window):
    players_on_fields = {i: [] for i in range(27)}
    
    # Populate the dictionary with players
    for player in players:
        players_on_fields[player.field].append(player.character)
    
    # Draw players above the fields
    for field, characters in players_on_fields.items():
        for idx, char in enumerate(characters):
            board_window.addstr(3 + 4 - idx - 1, (field * 2) + 2, char)
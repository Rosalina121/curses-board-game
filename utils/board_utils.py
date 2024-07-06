from random import randrange
from . import window_utils

def draw_board(stdscr, rows, cols, board_width, board_height):
    board_window = window_utils.draw_window(stdscr, board_height, board_width, x=0, y=0)

    # board_window.addstr(15, 5, f"Size: {rows}x{cols-22}")
    board_window.addstr(0, 1, "┤Teleturnieje Planszówka├")

    return board_window

def draw_board_play(board_array, board_window, unknown_char):
    for i in range(27):
        board_window.addstr(3 + 4, (i * 2) + 2, unknown_char if board_array[i].game is None else board_array[i].game)

def draw_board_players(players, board_window):
    window_utils.clear_rectangle(board_window, 2, 3, 27*2, 6)
    players_on_fields = {i: [] for i in range(27)}
    
    # Populate the dictionary with players
    for player in players:
        players_on_fields[player.field].append(player.character)
    
    # Draw players above the fields
    for field, characters in players_on_fields.items():
        for idx, char in enumerate(characters):
            board_window.addstr(3 + 4 - idx - 1, (field * 2) + 2, char)

def move_player(players, board_window, player, board_array, amount, unknown_char):
    player.field = (player.field + amount) % 27
    draw_board_players(players, board_window)
    drawn_game = draw_random_game(board_array, board_window, player.field, unknown_char)
    return drawn_game

def draw_random_game(board_array, board_window, field, unknown_char):
    games = ["M", "J", "1"]
    if board_array[field].game is None:
        board_array[field].game = games[randrange(len(games))]
        draw_board_play(board_array, board_window, unknown_char)
    return board_array[field].game

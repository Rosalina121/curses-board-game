from . import window_utils

from operator import attrgetter

def draw_leaderboard(stdscr, rows, cols, board_width, players, current_char):
    leaderboard_window = window_utils.draw_window(stdscr, rows - 10, 22, x=board_width, y=10)

    leaderboard_window.addstr(0, 1, "┤Leaderboard├")
    draw_leaderboard_scores(players, leaderboard_window, current_char)
    return leaderboard_window

def draw_leaderboard_scores(players, leaderboard_window, current_char):
    for player, p in zip(players, range(len(players))):
        leaderboard_window.addstr(2+p, 2, f"{current_char if player.current else ' '} {player.character} - {player.points}")

from . import window_utils

from operator import attrgetter

def draw_leaderboard(stdscr, rows, cols, board_width, players):
    leaderboard_window = window_utils.draw_window(stdscr, rows - 10, 22, x=board_width, y=10)

    leaderboard_window.addstr(0, 1, "┤Leaderboard├")
    draw_leaderboard_scores(players, leaderboard_window)
    return leaderboard_window

def draw_leaderboard_scores(players, leaderboard_window):
    for player, p in zip(sorted(players, key=attrgetter("points"), reverse=True), range(len(players))):
        leaderboard_window.addstr(2+p, 2, f"{'>' if player.current else ' '} {player.character} - {player.points}")

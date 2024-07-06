import curses
import curses.panel

from random import randrange
import time
import sys

import argparse

from enitites.board_field import BoardField
from enitites.player import Player

import utils.board_utils as board_utils
import utils.loeaderboard_utils as leaderboard_utils
import utils.roll_utils as roll_utils
import utils.window_utils as window_utils
import utils.game_utils as game_utils

from utils.character_utils import Characters


# TODO
# current player
# show current player oon the leaderboard
# fill leaderboard with players from set
# NerdFont mode
# Custom players like -c "#@%"
def main():
    ex = "Thanks for playing!"

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--custom", help="Custom players chars to use", type=str)
    parser.add_argument(
        "-n", "--nerd-font", help="Enable Nerd Font", action="store_true"
    )
    parser.add_argument("--foo", help="foo help")
    args = parser.parse_args()

    # setup curses
    stdscr = None
    rows, cols = 0, 0
    # nerdfont?
    nerd_font = args.nerd_font
    char = Characters(nerd_font=args.nerd_font)
    # game stuctures
    # board array of board_field, size is 27
    board_array = [BoardField() for _ in range(27)]

    # players
    players = list()
    player_symbols = []
    if args.custom:
        player_symbols = args.custom
    else:
        player_symbols = char.default_players()
    for symbol in player_symbols:
        players.append(Player(symbol, field=0))

    # set random player current = True
    players[0].current = True

    # turn lock
    turn_lock = False

    try:
        stdscr = setup_curses()
        rows, cols = stdscr.getmaxyx()
        if rows < 20 or cols < 100:
            raise Exception("Terminal must be at least 20x100")

        # setup windows
        # roll and leaderboard are 20 cols (22 with padding for border)
        # roll is 8 high (10 with padding for border)
        board_width = cols - 22
        board_height = rows - 10

        board_window = board_utils.draw_board(
            stdscr, rows, cols, board_width, board_height
        )
        leaderboard_window = leaderboard_utils.draw_leaderboard(
            stdscr, rows, cols, board_width, players, char.current_player()
        )
        roll_window = roll_utils.draw_roll(stdscr, board_width, char.nerd_font)
        game_window = game_utils.draw_game(stdscr, board_height, board_width)

        board_utils.draw_board_play(board_array, board_window, char.unknown_question())
        board_utils.draw_board_players(players, board_window)

        # draw_border(stdscr)
        while True:
            key = stdscr.getch()

            if key == ord("r") and not turn_lock:
                turn_lock = True

                # perform turn
                roll = roll_utils.roll_dice(roll_window, char.nerd_font)
                current_player = next(
                    (player for player in players if player.current), None
                )
                game = board_utils.move_player(
                    players,
                    board_window,
                    current_player,
                    board_array,
                    roll,
                    char.unknown_question(),
                )

                # do stuff with game
                game_utils.draw_new_game(game_window, game)
                game_window.addstr(2, 2, f"Wait...")
                # TODO
                time.sleep(2)
                game_window.addstr(2, 2, f"Done!  ")

                # next player
                for player in players:
                    player.current = False
                players[(players.index(current_player) + 1) % len(players)].current = (
                    True
                )
                leaderboard_utils.draw_leaderboard_scores(
                    players, leaderboard_window, char.current_player()
                )

                curses.flushinp()
                turn_lock = False

            elif key == ord("q"):
                break
            elif key == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()

                # Roll! button: TBD
                # if x >= 91 and x <= 95 and y == 7:
                #     roll_utils.roll_dice(roll_window)
                # board_window.addstr(3, 2, f"({x}, {y})")

    # except Exception as e:
    #     ex = e
    finally:
        close(stdscr)
        print(ex)


def close(stdscr):
    if stdscr is not None:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()


def setup_curses():
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)
    curses.mousemask(1)
    curses.curs_set(0)
    curses.cbreak()
    stdscr.nodelay(True)
    return stdscr


def draw_border(stdscr):
    stdscr.border(0)
    stdscr.refresh()


if __name__ == "__main__":
    main()

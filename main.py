import curses
import time

from random import randrange
from operator import attrgetter
from itertools import groupby


from board_field import BoardField
from player import Player


def main():
    ex = "Thanks for playing!"

    # setup curses
    stdscr = None
    rows, cols = 0, 0

    # game stuctures
    # board array of board_field, size is 27
    board_array = [BoardField("O", set()) for _ in range(27)]

    # players
    players = set()
    player_symbols = ["$", "#", "@", "%"]
    for symbol in player_symbols:
        players.add(Player(symbol, field=randrange(0, 27)))

    try:
        stdscr = setup_curses()
        rows, cols = stdscr.getmaxyx()
        if rows < 20 or cols < 100:
            raise Exception("Terminal must be at least 20x100")

        # setup windows
        # roll and leaderboard are 20 cols (22 with padding for border)
        # roll is 8 high (10 with padding for border)
        board_width = cols - 22

        board_window = draw_board(stdscr, rows, cols, board_width)
        leaderboard_window = draw_leaderboard(stdscr, rows, cols, board_width)
        roll_window = draw_roll(stdscr, rows, cols, board_width)

        draw_board_play(board_array, board_window)
        draw_board_players(players, board_window)

        # draw_border(stdscr)
        while True:
            key = stdscr.getch()
            if key == ord("r"):
                roll_dice(roll_window)
            elif key == ord("q"):
                break
            elif key == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()

                # Roll! button: x=91-95, y=7
                if x >= 91 and x <= 95 and y == 7:
                    roll_dice(roll_window)
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
    return stdscr


def draw_border(stdscr):
    stdscr.border(0)
    stdscr.refresh()


def draw_window(stdscr, rows, cols, x, y):
    window = stdscr.subwin(rows, cols, y, x)
    window.immedok(True)
    window.box()
    window.border(0)
    window.refresh()
    return window


def draw_board(stdscr, rows, cols, board_width):
    board_window = draw_window(stdscr, rows, board_width, x=0, y=0)

    board_window.addstr(15, 5, f"{rows}x{cols-22}")
    board_window.addstr(0, 1, "┤Teleturnieje Planszówka├")

    return board_window


def draw_leaderboard(stdscr, rows, cols, board_width):
    leaderboard_window = draw_window(stdscr, rows - 10, 22, x=board_width, y=10)

    leaderboard_window.addstr(0, 1, "┤Leaderboard├")
    leaderboard_window.addstr(2, 2, "$ - 0")
    leaderboard_window.addstr(3, 2, "@ - 0")
    leaderboard_window.addstr(4, 2, "# - 0")
    leaderboard_window.addstr(5, 2, "% - 0")
    return leaderboard_window


def draw_roll(stdscr, rows, cols, board_width):
    roll_window = draw_window(stdscr, 10, 22, x=board_width, y=0)

    roll_window.addstr(0, 1, "┤Roll├")
    roll_window.addstr(1, 2, "┏━━━━━━━┓")
    roll_window.addstr(2, 2, "┃ •   • ┃")
    roll_window.addstr(3, 2, "┃   •   ┃")
    roll_window.addstr(4, 2, "┃ •   • ┃")
    roll_window.addstr(5, 2, "┗━━━━━━━┛")

    roll_window.addstr(7, 13, "Roll!", curses.A_REVERSE)
    return roll_window


def roll_dice(roll_window):
    def print_one():
        roll_window.addstr(2, 2, "┃       ┃")
        roll_window.addstr(3, 2, "┃   •   ┃")
        roll_window.addstr(4, 2, "┃       ┃")

    def print_two():
        roll_window.addstr(2, 2, "┃     • ┃")
        roll_window.addstr(3, 2, "┃       ┃")
        roll_window.addstr(4, 2, "┃ •     ┃")

    def print_three():
        roll_window.addstr(2, 2, "┃     • ┃")
        roll_window.addstr(3, 2, "┃   •   ┃")
        roll_window.addstr(4, 2, "┃ •     ┃")

    def print_four():
        roll_window.addstr(2, 2, "┃ •   • ┃")
        roll_window.addstr(3, 2, "┃       ┃")
        roll_window.addstr(4, 2, "┃ •   • ┃")

    def print_five():
        roll_window.addstr(2, 2, "┃ •   • ┃")
        roll_window.addstr(3, 2, "┃   •   ┃")
        roll_window.addstr(4, 2, "┃ •   • ┃")

    def print_six():
        roll_window.addstr(2, 2, "┃ •   • ┃")
        roll_window.addstr(3, 2, "┃ •   • ┃")
        roll_window.addstr(4, 2, "┃ •   • ┃")

    # get random between 1 and 6
    result = randrange(1, 6)

    print_one()
    time.sleep(0.1)
    print_two()
    time.sleep(0.2)
    print_three()
    time.sleep(0.3)
    print_four()
    time.sleep(0.1)
    print_five()
    time.sleep(0.3)
    print_six()
    time.sleep(0.2)

    match result:
        case 1:
            print_one()
        case 2:
            print_two()
        case 3:
            print_three()
        case 4:
            print_four()
        case 5:
            print_five()
        case 6:
            print_six()


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

if __name__ == "__main__":
    main()

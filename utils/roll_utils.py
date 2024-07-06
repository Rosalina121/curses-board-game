from . import window_utils

from random import randrange
import time
import curses

def draw_roll(stdscr, rows, cols, board_width):
    roll_window = window_utils.draw_window(stdscr, 10, 22, x=board_width, y=0)

    roll_window.addstr(0, 1, "┤Roll├")
    roll_window.addstr(1, 2, "┏━━━━━━━┓")
    roll_window.addstr(2, 2, "┃ •   • ┃")
    roll_window.addstr(3, 2, "┃   •   ┃")
    roll_window.addstr(4, 2, "┃ •   • ┃")
    roll_window.addstr(5, 2, "┗━━━━━━━┛")

    roll_window.addstr(7, 13, "R", curses.A_REVERSE)
    roll_window.addstr(7, 14, "oll!")

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
        roll_window.addstr(2, 2, "┃ •     ┃")
        roll_window.addstr(3, 2, "┃   •   ┃")
        roll_window.addstr(4, 2, "┃     • ┃")

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

    dice_prints = [
        print_one,
        print_two,
        print_three,
        print_four,
        print_five,
        print_six
    ]
    for rolls in range(13):
        dice_prints[randrange(0, 6)]()
        time.sleep(0.02 * rolls)

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

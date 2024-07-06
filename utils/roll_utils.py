from . import window_utils

from random import randrange
import time
import curses

def draw_roll(stdscr, board_width, nerd_font):
    roll_window = window_utils.draw_window(stdscr, 10, 22, x=board_width, y=0)

    roll_window.addstr(0, 1, "┤")
    roll_window.addstr(0, 2, "R", curses.A_UNDERLINE)
    roll_window.addstr(0, 3, "oll├")
    if nerd_font:
        roll_window.addstr(1, 3, "┏━━━━━━━━━━━━━━┓")
        roll_window.addstr(2, 3, "┃          ┃")        
        roll_window.addstr(3, 3, "┃              ┃")
        roll_window.addstr(4, 3, "┃            ┃")
        roll_window.addstr(5, 3, "┃              ┃")
        roll_window.addstr(6, 3, "┃          ┃")
        roll_window.addstr(7, 3, "┗━━━━━━━━━━━━━━┛")
        roll_window.addstr(8, 3, " 󰇎")
    else:
        roll_window.addstr(1, 3, "┏━━━━━━━━━━━━━━┓")
        roll_window.addstr(2, 3, "┃              ┃")
        roll_window.addstr(3, 3, "┃  ██      ██  ┃")
        roll_window.addstr(4, 3, "┃      ▄▄      ┃")
        roll_window.addstr(5, 3, "┃      ▀▀      ┃")
        roll_window.addstr(6, 3, "┃  ██      ██  ┃")
        roll_window.addstr(7, 3, "┃              ┃")
        roll_window.addstr(8, 3, "┗━━━━━━━━━━━━━━┛")

    return roll_window


def roll_dice(roll_window, nerd_font):
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
        dice_prints[randrange(0, 6)](roll_window, nerd_font)
        time.sleep(0.02 * rolls)

    match result:
        case 1:
            print_one(roll_window, nerd_font)
        case 2:
            print_two(roll_window, nerd_font)
        case 3:
            print_three(roll_window, nerd_font)
        case 4:
            print_four(roll_window, nerd_font)
        case 5:
            print_five(roll_window, nerd_font)
        case 6:
            print_six(roll_window, nerd_font)

    return result

def print_one(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃              ┃")
        roll_window.addstr(4, 3, "┃            ┃")
        roll_window.addstr(6, 3, "┃              ┃")

        roll_window.addstr(8, 3, "  󰇊             ")

    else:
        roll_window.addstr(3, 3, "┃              ┃")
        roll_window.addstr(4, 3, "┃      ▄▄      ┃")
        roll_window.addstr(5, 3, "┃      ▀▀      ┃")
        roll_window.addstr(6, 3, "┃              ┃")

def print_two(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃            ┃")
        roll_window.addstr(4, 3, "┃              ┃")
        roll_window.addstr(6, 3, "┃            ┃")

        roll_window.addstr(8, 3, "    󰇋           ")

    else:
        roll_window.addstr(3, 3, "┃          ██  ┃")
        roll_window.addstr(4, 3, "┃              ┃")
        roll_window.addstr(5, 3, "┃              ┃")
        roll_window.addstr(6, 3, "┃  ██          ┃")
def print_three(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃            ┃")
        roll_window.addstr(4, 3, "┃            ┃")
        roll_window.addstr(6, 3, "┃            ┃")

        roll_window.addstr(8, 3, "      󰇌         ")

    else:
        roll_window.addstr(3, 3, "┃  ██          ┃")
        roll_window.addstr(4, 3, "┃      ▄▄      ┃")
        roll_window.addstr(5, 3, "┃      ▀▀      ┃")
        roll_window.addstr(6, 3, "┃          ██  ┃")

def print_four(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃          ┃")
        roll_window.addstr(4, 3, "┃              ┃")
        roll_window.addstr(6, 3, "┃          ┃")

        roll_window.addstr(8, 3, "        󰇍       ")

    else:
        roll_window.addstr(3, 3, "┃  ██      ██  ┃")
        roll_window.addstr(4, 3, "┃              ┃")
        roll_window.addstr(5, 3, "┃              ┃")
        roll_window.addstr(6, 3, "┃  ██      ██  ┃")

def print_five(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃          ┃")
        roll_window.addstr(4, 3, "┃            ┃")
        roll_window.addstr(6, 3, "┃          ┃")

        roll_window.addstr(8, 3, "          󰇎     ")

    else:
        roll_window.addstr(3, 3, "┃  ██      ██  ┃")
        roll_window.addstr(4, 3, "┃      ▄▄      ┃")
        roll_window.addstr(5, 3, "┃      ▀▀      ┃")
        roll_window.addstr(6, 3, "┃  ██      ██  ┃")

def print_six(roll_window, nerd_font):
    if nerd_font:
        roll_window.addstr(2, 3, "┃          ┃")
        roll_window.addstr(4, 3, "┃          ┃")
        roll_window.addstr(6, 3, "┃          ┃")

        roll_window.addstr(8, 3, "            󰇏   ")

    else:
        roll_window.addstr(3, 3, "┃  ██      ██  ┃")
        roll_window.addstr(4, 3, "┃  ▄▄      ▄▄  ┃")
        roll_window.addstr(5, 3, "┃  ▀▀      ▀▀  ┃")
        roll_window.addstr(6, 3, "┃  ██      ██  ┃")

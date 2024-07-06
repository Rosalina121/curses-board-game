import curses
from random import randrange



from enitites.board_field import BoardField
from enitites.player import Player

import utils.board_utils as board_utils
import utils.loeaderboard_utils as leaderboard_utils
import utils.roll_utils as roll_utils



# TODO
# current player
# show current player oon the leaderboard
# fill leaderboard with players from set
# NerdFont mode
# Custom players like -c "#@%"
def main():
    ex = "Thanks for playing!"

    # setup curses
    stdscr = None
    rows, cols = 0, 0

    # game stuctures
    # board array of board_field, size is 27
    board_array = [BoardField("O", set()) for _ in range(27)]

    # players
    players = list()
    player_symbols = ["$", "#", "@", "%"]
    for symbol in player_symbols:
        players.append(Player(symbol, field=0))

    # set random player current = True
    players[randrange(len(players))].current = True
    

    try:
        stdscr = setup_curses()
        rows, cols = stdscr.getmaxyx()
        if rows < 20 or cols < 100:
            raise Exception("Terminal must be at least 20x100")

        # setup windows
        # roll and leaderboard are 20 cols (22 with padding for border)
        # roll is 8 high (10 with padding for border)
        board_width = cols - 22

        board_window = board_utils.draw_board(stdscr, rows, cols, board_width)
        leaderboard_window = leaderboard_utils.draw_leaderboard(stdscr, rows, cols, board_width, players)
        roll_window = roll_utils.draw_roll(stdscr, rows, cols, board_width)

        board_utils.draw_board_play(board_array, board_window)
        board_utils.draw_board_players(players, board_window)

        # draw_border(stdscr)
        while True:
            key = stdscr.getch()
            if key == ord("r"):
                roll_utils.roll_dice(roll_window)
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
    return stdscr


def draw_border(stdscr):
    stdscr.border(0)
    stdscr.refresh()


if __name__ == "__main__":
    main()

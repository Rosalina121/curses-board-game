import curses
from random import randrange
import random
import textwrap
import time
import yaml

from . import window_utils


def draw_game(stdscr, rows, cols):
    game_window = window_utils.draw_window(stdscr, rows, cols, x=0, y=rows)

    game_window.addstr(0, 1, "┤Gra: ???├")
    # game_window.addstr(1, 2, game)
    return game_window


def draw_new_game(game_window, game, board_width, board_height, player):
    game_window.erase()
    game_window.border(0)
    if game == "M":
        draw_milionerzy(game_window, board_width, board_height, player)
    elif game == "1":
        draw_1z10(game_window)
    elif game == "J":
        draw_jaka_to_melodia(game_window)
    return


def draw_milionerzy(game_window, board_width, board_height, player):
    game_window.addstr(0, 1, "Gra: Milionerzy├")
    questions = None
    with open("game_questions/milionerzy.yaml", "r") as stream:
        try:
            questions = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    random_question = questions[randrange(len(questions))]

    question = random_question["question"]
    question_reward = random.choice([500, 1000, 2000])
    ans_a = random_question["ans"][0]
    ans_b = random_question["ans"][1]
    ans_c = random_question["ans"][2]
    ans_d = random_question["ans"][3]
    correct_ans = random_question["correct_ans"]

    selected_ans = None

    # Prepare the question to be displayed centered and split if necessary
    wrapped_text = textwrap.wrap(question, 66)
    if len(wrapped_text) > 2:
        wrapped_text = wrapped_text[:2]  # If more than 2 lines, truncate to 2 lines

    line1 = wrapped_text[0].center(66)
    line2 = wrapped_text[1].center(66) if len(wrapped_text) > 1 else ""

    # [ Pytanie ]
    # [ A:   B: ]
    # [ C:   D: ]

    # Draw question
    game_window.addstr(2, 4, "╱")
    game_window.addstr(3, 4, "╲")
    game_window.addstr(2, 1, "   ", curses.A_UNDERLINE)
    game_window.addstr(2, board_width - 5, "╲")
    game_window.addstr(3, board_width - 5, "╱")
    game_window.addstr(2, board_width - 4, "   ", curses.A_UNDERLINE)

    # Add centered question split between 2 lines if necessary
    game_window.addstr(2, (board_width - 66) // 2, line1)
    game_window.addstr(3, (board_width - 66) // 2, line2)

    # Draw reward
    game_window.addstr(
        8, board_width - len(f"ᐸ Nagroda: {question_reward} ᐳ") - 2, f"ᐸ"
    )
    game_window.addstr(
        8,
        board_width - len(f"ᐸ Nagroda: {question_reward} ᐳ") - 1,
        f" Nagroda: {question_reward} ",
        curses.A_UNDERLINE,
    )
    game_window.addstr(8, board_width - 3, f"ᐳ")

    # draw answers
    def draw_ans():
        milionerzy_draw_answer(game_window, ans_a, "A", board_width)
        milionerzy_draw_answer(game_window, ans_b, "B", board_width)
        milionerzy_draw_answer(game_window, ans_c, "C", board_width)
        milionerzy_draw_answer(game_window, ans_d, "D", board_width)

    draw_ans()

    while True:
        test = game_window.getch()
        if test == ord("a"):
            draw_ans()
            selected_ans = milionerzy_draw_answer(
                game_window, ans_a, "A", board_width, highlight=True
            )
        elif test == ord("b"):
            draw_ans()
            selected_ans = milionerzy_draw_answer(
                game_window, ans_b, "B", board_width, highlight=True
            )
        elif test == ord("c"):
            draw_ans()
            selected_ans = milionerzy_draw_answer(
                game_window, ans_c, "C", board_width, highlight=True
            )
        elif test == ord("d"):
            draw_ans()
            selected_ans = milionerzy_draw_answer(
                game_window, ans_d, "D", board_width, highlight=True
            )
        elif test == ord(" "):
            if selected_ans:
                if selected_ans == correct_ans:
                    game_window.addstr(
                        8, 2, " Brawo! Poprawna odpowiedź! ", curses.A_REVERSE
                    )
                    player.points += question_reward
                else:
                    game_window.addstr(
                        8,
                        2,
                        f" Zła odpowiedź! Poprawną było: {correct_ans} ",
                        curses.A_REVERSE,
                    )
                break

    time.sleep(3)
    game_window.erase()
    game_window.border(0)
    game_window.addstr(0, 1, "┤Game: ???├")
    return


def milionerzy_draw_answer(
    game_window, ans_text, ans_letter, board_width, highlight=False
):
    style = curses.A_REVERSE if highlight else curses.A_UNDERLINE
    ans_width = int((board_width - 2) / 2)

    x, y = 0, 0
    if ans_letter == "A" or ans_letter == "C":
        y = 5 if ans_letter == "A" else 6

        game_window.addstr(y, 1, "─ᐸ")  # canadian syllabics ᐸ
        game_window.addstr(y, 3, f" {ans_letter}: ", style)  # it's nbsp btw
        game_window.addstr(y, 7, ans_text, style)
        game_window.addstr(
            y,
            7 + len(ans_text),
            " " * (ans_width - 7 - len(ans_text)),
            style,
        )
        game_window.addstr(y, ans_width - 2, "ᐳ─")

    else:
        y = 5 if ans_letter == "B" else 6

        game_window.addstr(y, ans_width, "ᐸ")
        game_window.addstr(y, ans_width + 1, f" {ans_letter}: ", style)
        game_window.addstr(y, ans_width + 5, ans_text, style)
        game_window.addstr(
            y,
            ans_width + 5 + len(ans_text),
            " " * (ans_width - 6 - len(ans_text)),
            style,
        )
        game_window.addstr(y, ans_width + ans_width - 1, "ᐳ─")

    if highlight:
        game_window.addstr(8, 2, "Definitywnie? (")
        game_window.addstr(8, 2 + len("Definitywnie? ("), "SPACJA", curses.A_UNDERLINE)
        game_window.addstr(8, 2 + len("Definitywnie? (SPACJA"), ")")

        return ans_letter


def draw_1z10(game_window):
    game_window.addstr(0, 1, "┤Game: 1 z 10├")


def draw_jaka_to_melodia(game_window):
    game_window.addstr(0, 1, "┤Game: Jaka to Melodia?├")

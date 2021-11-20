from consts import *
from pandas import *


def pretty_print_board(board: list) -> None:
    # pandas header feature is off center so this is needed
    if NUM_MINES == 10:
        print(SMALL_HEADERS)
    elif NUM_MINES == 40:
        print(MEDIUM_HEADERS)
    elif NUM_MINES == 99:
        print(LARGE_HEADERS)
    print(DataFrame(data=board).to_string(index=True, header=False))


def print_seperator() -> None:
    print(SEPERATOR)


def print_game_over(board: list) -> None:
    print_seperator()
    print(GAME_OVER)
    pretty_print_board(board)
    print_seperator()


def print_game_won(board: list) -> None:
    print_seperator()
    print(GAME_WON)
    pretty_print_board(board)
    print_seperator()

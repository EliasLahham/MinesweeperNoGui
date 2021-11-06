from pandas import *
from consts import NUM_MINES, SMALL_HEADERS, MEDIUM_HEADERS, LARGE_HEADERS, SEPERATOR


def pretty_print_board(board):
    # pandas header feature is off center so this is needed
    if NUM_MINES == 10:
        print(SMALL_HEADERS)
    elif NUM_MINES == 40:
        print(MEDIUM_HEADERS)
    elif NUM_MINES == 99:
        print(LARGE_HEADERS)
    print(DataFrame(data=board).to_string(index=True, header=False))


def print_seperator():
    print(SEPERATOR)


def print_game_over(board):
    print('GAME OVER!')
    pretty_print_board(board)

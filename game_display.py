from pandas import *


def print_seperator():
    print('=====================================================')


def print_game_over(board):
    print('GAME OVER!')
    pretty_print_board(board)


def pretty_print_board(board):
    print('    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17')
    print(DataFrame(data=board).to_string(index=True, header=False))

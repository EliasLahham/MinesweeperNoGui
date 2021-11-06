from board_helper import Revealed_Tile, get_adjacent_indices, get_adjacent_bomb_count, not_starting_tile, not_surrounding_starting_tile, get_solved_board_value, should_reveal_more, get_revealed_tiles, reveal_tiles
from consts import ROWS, COLUMNS, NUM_MINES
import random


def build_empty_board_with_mines(starting_tile):
    board = build_empty_board('▯')
    starting_adjacent_indices = get_adjacent_indices(starting_tile[0], starting_tile[1])
    i = 0

    while i < NUM_MINES:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLUMNS - 1)
        if (board[row][col] != '*' and
                not_surrounding_starting_tile(starting_adjacent_indices, row, col) is True and
                not_starting_tile(starting_tile, row, col)):
            adjacent_indices = get_adjacent_indices(row, col)
            for index in adjacent_indices:
                if board[index[0]][index[1]] == '▯':  # Prevents unreachable mines
                    board[row][col] = '*'
                    i += 1
                    break

    return board


def build_empty_board(empty_tile_indicator):
    return [[empty_tile_indicator for col in range(COLUMNS)] for row in range(ROWS)]


def build_solved_board(empty_board_with_mines):
    solved_board = build_empty_board('_')

    for row in range(ROWS):
        for col in range(COLUMNS):
            if empty_board_with_mines[row][col] != '*':
                adjacent_indices = get_adjacent_indices(row, col)
                solved_board[row][col] = get_adjacent_bomb_count(
                    adjacent_indices, empty_board_with_mines)
            else:
                solved_board[row][col] = '*'

    return solved_board


def build_play_board_with_revealed_tile(play_board, solved_board, chosen_tile):
    tile_to_reveal = Revealed_Tile(
        chosen_tile[0],
        chosen_tile[1],
        should_reveal_more(solved_board, chosen_tile[0], chosen_tile[1]),
        get_solved_board_value(solved_board, chosen_tile[0], chosen_tile[1]))
    if tile_to_reveal.check_adjacent:
        tiles_to_reveal = get_revealed_tiles(solved_board, tile_to_reveal)
        play_board = reveal_tiles(play_board, tiles_to_reveal)
    else:
        play_board[chosen_tile[0]][chosen_tile[1]] = tile_to_reveal.shown_value
    return play_board

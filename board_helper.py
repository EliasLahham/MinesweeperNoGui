from consts import *


class Revealed_Tile:
    def __init__(self, row, col, check_adjacent, shown_value):
        self.row = row
        self.col = col
        self.check_adjacent = check_adjacent
        self.shown_value = shown_value


def get_adjacent_indices(row, col):
    adjacent_indices = []
    if row > 0:
        adjacent_indices.append((row - 1, col))
    if row + 1 < ROWS:
        adjacent_indices.append((row + 1, col))
    if col > 0:
        adjacent_indices.append((row, col - 1))
    if col + 1 < COLUMNS:
        adjacent_indices.append((row, col + 1))
    if row - 1 >= 0 and col + 1 < COLUMNS:
        adjacent_indices.append((row - 1, col + 1))
    if row + 1 < ROWS and col - 1 >= 0:
        adjacent_indices.append((row + 1, col - 1))
    if row - 1 >= 0 and col - 1 >= 0:
        adjacent_indices.append((row - 1, col - 1))
    if row + 1 < ROWS and col + 1 < COLUMNS:
        adjacent_indices.append((row + 1, col + 1))
    return adjacent_indices


def not_surrounding_starting_tile(starting_adjacent_indices, random_row, random_col):
    for index in starting_adjacent_indices:
        if index[0] == random_row and index[1] == random_col:
            return False
    return True


def not_starting_tile(starting_tile, random_row, random_col):
    if starting_tile[0] == random_row and starting_tile[1] == random_col:
        return False
    return True


def get_adjacent_mine_count(adjacent_indices, empty_board_with_mines):
    adjacent_mine_count = 0

    for index in adjacent_indices:
        if empty_board_with_mines[index[0]][index[1]] == '*':
            adjacent_mine_count += 1

    return str(adjacent_mine_count) if adjacent_mine_count > 0 else '_'


def should_reveal_more(solved_board, row, col):
    if solved_board[row][col] == '_':
        return True
    return False


def get_solved_board_value(solved_board, row, col):
    return solved_board[row][col]


def get_revealed_tiles(solved_board, tile_to_reveal):
    tiles_left_to_check = 1  # Starts with 1 because incoming tile is being checked
    checked_tiles = set()
    tiles_to_reveal = []
    tiles_to_reveal.append(tile_to_reveal)
    while tiles_left_to_check > 0:
        for tile in tiles_to_reveal:
            if tile.check_adjacent:
                adjacent_indices = get_adjacent_indices(tile.row, tile.col)
                for index in adjacent_indices:
                    check_adjacent = should_reveal_more_if_not_checked(solved_board, index[0], index[1], checked_tiles)
                    tiles_to_reveal.append(Revealed_Tile(index[0], index[1], check_adjacent, get_solved_board_value(solved_board, index[0], index[1])))
                    tiles_left_to_check = get_tiles_left_to_check_count(check_adjacent, tiles_left_to_check)
                checked_tiles.add((tile.row, tile.col))
    return tiles_to_reveal


def should_reveal_more_if_not_checked(solved_board, row, col, checked_tiles):
    if not (row, col) in checked_tiles and solved_board[row][col] == '_':
        return True
    return False


def get_tiles_left_to_check_count(check_adjacent, tiles_left_to_check):
    if check_adjacent:
        tiles_left_to_check += 1
    else:
        tiles_left_to_check -= 1
    return tiles_left_to_check


def reveal_tiles(play_board, tiles_to_reveal):
    for tile in tiles_to_reveal:
        play_board[tile.row][tile.col] = tile.shown_value
    return play_board


def has_player_won(play_board, mine_locations):
    for mine in mine_locations:
        if play_board[mine[0]][mine[1]] != '^':
            return False
    return True

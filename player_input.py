from consts import *


class Chosen_Tile:
    def __init__(self, row, col, flag, unflag):
        self.row = row
        self.col = col
        self.flag = flag
        self.unflag = unflag


def get_starting_tile():
    starting_tile = get_user_input()

    while is_valid_tile(starting_tile[0], starting_tile[1], None, None) is False:
        print(TILE_NOT_VALID)
        starting_tile = get_user_input()

    return starting_tile


def get_user_input():
    row = input(PICK_ROW)
    while row.isnumeric() is False:
        row = input(PICK_ROW)

    col = input(PICK_COL)
    while col.isnumeric() is False:
        col = input(PICK_COL)

    return (int(row), int(col))


def is_valid_tile(row, col, play_board, is_unflagging):
    if ((col >= 0 and col < COLUMNS) and
            (row >= 0 and row < ROWS)):
        if (((play_board and play_board[row][col] == '▯') or
                (play_board and play_board[row][col] == '^' and is_unflagging)) or
                not play_board and not is_unflagging):  # This last check is only when the starting tile is selected
            return True
    return False


def get_chosen_tile_and_decision(play_board):
    is_flagging = is_user_flagging()
    is_unflagging = is_user_unflagging(is_flagging)
    chosen_tile = get_user_input()
    while is_valid_tile(chosen_tile[0], chosen_tile[1], play_board, is_unflagging) is False:
        print(TILE_NOT_VALID)
        chosen_tile = get_user_input()
    return Chosen_Tile(chosen_tile[0], chosen_tile[1], is_flagging, is_unflagging)


def is_user_flagging():
    decision = input(PICK_FLAG)
    if decision.lower() == 'y':
        return True
    return False


def is_user_unflagging(is_flagging):
    if is_flagging is False:
        decision = input(PICK_UNFLAG)
        if decision.lower() == 'y' and is_flagging is False:
            return True
    return False

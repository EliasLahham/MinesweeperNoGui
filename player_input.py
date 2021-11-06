from consts import ROWS, COLUMNS


class Chosen_Tile:
    def __init__(self, row, col, flag, unflag):
        self.row = row
        self.col = col
        self.flag = flag
        self.unflag = unflag


def get_starting_tile():
    starting_tile = get_user_input()

    while is_valid_tile(starting_tile[0], starting_tile[1], None) is False:
        print('Tile not valid')
        starting_tile = get_user_input()

    return starting_tile
    

def is_valid_tile(row, col, play_board):
    if ((col >= 0 and col <= COLUMNS - 1) and
            (row >= 0 and row <= ROWS - 1)):
        if ((play_board and play_board[row][col] == '▯') or
            not play_board):
            return True
    return False


def get_chosen_tile_and_decision(play_board):
    chosen_tile = get_user_input()
    while is_valid_tile(chosen_tile[0], chosen_tile[1], play_board) is False:
        print('Tile out of bounds or already checked. Pick again...')
        chosen_tile = get_user_input()
    is_flagging = is_user_flagging()
    is_unflagging = is_user_unflagging(is_flagging)
    return Chosen_Tile(chosen_tile[0], chosen_tile[1], is_flagging, is_unflagging)


def get_user_input():
    row = input('Pick a row: ')
    while row.isnumeric() is False:
        row = input('Pick a row: ')

    col = input('Pick a column: ')
    while col.isnumeric() is False:
        col = input('Pick a column: ')

    return (int(row), int(col))


def is_user_flagging():
    decision = input('Type Y to flag your selected tile or anything else to not flag: ')
    if decision.lower() == 'y':
        return True
    return False


def is_user_unflagging(is_flagging):
    decision = input('Type Y to unflag your selected tile or anything else to not unflag: ')
    if decision.lower() == 'y' and is_flagging is False:
        return True
    elif decision.lower() == 'y' and is_flagging is True:
        print("You're already flagging, you cannot unflag. Flag placed...")  # Add something here to let user revert their decision
    return False

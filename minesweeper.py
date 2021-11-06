from board_builder import build_empty_board, build_empty_board_with_mines, build_solved_board
from player_input import get_starting_tile
from game_display import pretty_print_board
from player import play_game


def main():
    empty_board, solved_board, starting_tile, mine_locations = setup_game()
    play_game(empty_board, solved_board, starting_tile, mine_locations)


def setup_game():
    empty_board = build_empty_board('▯')
    pretty_print_board(empty_board)
    starting_tile = get_starting_tile()
    empty_board_with_mines, mine_locations = build_empty_board_with_mines(starting_tile)
    solved_board = build_solved_board(empty_board_with_mines)
    return empty_board, solved_board, starting_tile, mine_locations


if __name__ == '__main__':
    main()

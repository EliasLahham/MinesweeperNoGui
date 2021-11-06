from player_input import get_starting_tile
from board_builder import build_empty_board_with_mines, build_solved_board
from game_display import pretty_print_board
from player import play_game


def main():
    starting_tile = get_starting_tile()
    empty_board_with_mines = build_empty_board_with_mines(starting_tile)
    solved_board = build_solved_board(empty_board_with_mines)
    # pretty_print_board(solved_board)
    play_game(empty_board_with_mines, solved_board, starting_tile)


if __name__ == '__main__':
    main()

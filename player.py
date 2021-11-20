from board_builder import build_play_board_with_revealed_tile
from game_display import print_seperator, pretty_print_board, print_game_over, print_game_won
from player_input import get_chosen_tile_and_decision
from board_helper import has_player_won


def play_game(empty_board: list, solved_board: list, starting_tile: tuple, mine_locations) -> None:
    play_board = build_play_board_with_revealed_tile(empty_board, solved_board, starting_tile)
    while True:
        print_seperator()
        pretty_print_board(play_board)
        chosen_tile_and_decision = get_chosen_tile_and_decision(play_board)
        if chosen_tile_and_decision.flag:  # Player is placing flag
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '^'
        elif chosen_tile_and_decision.unflag:  # Player is removing flag
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '▯'
        elif (chosen_tile_and_decision.flag is False and chosen_tile_and_decision.unflag is False and  # Checking if mine was hit
                (chosen_tile_and_decision.row, chosen_tile_and_decision.col) in mine_locations):
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '*'
            print_game_over(play_board)
            break
        else:  # Reveal chosen tile(s)
            play_board = build_play_board_with_revealed_tile(play_board, solved_board, (chosen_tile_and_decision.row, chosen_tile_and_decision.col))

        if has_player_won(play_board, mine_locations):
            print_game_won(play_board)
            break

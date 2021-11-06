from board_helper import get_bomb_locations, was_mine_hit, has_player_won
from board_builder import build_empty_board, build_play_board_with_revealed_tile
from game_display import pretty_print_board, print_game_over, print_seperator
from player_input import get_chosen_tile_and_decision


def play_game(empty_board_with_mines, solved_board, starting_tile):
    bomb_locations = get_bomb_locations(empty_board_with_mines)
    play_board = build_play_board_with_revealed_tile(build_empty_board('▯'), solved_board, starting_tile)
    while True:
        print_seperator()
        pretty_print_board(play_board)
        chosen_tile_and_decision = get_chosen_tile_and_decision(play_board)
        if chosen_tile_and_decision.flag:
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '^'
        elif chosen_tile_and_decision.unflag:
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '▯'
        elif (chosen_tile_and_decision.flag is False and chosen_tile_and_decision.unflag is False and
                was_mine_hit((chosen_tile_and_decision.row, chosen_tile_and_decision.col), bomb_locations)):
            play_board[chosen_tile_and_decision.row][chosen_tile_and_decision.col] = '*'
            print_game_over(play_board)
            break
        else:
            play_board = build_play_board_with_revealed_tile(play_board, solved_board, (chosen_tile_and_decision.row, chosen_tile_and_decision.col))

        if has_player_won(play_board, bomb_locations):
            print_seperator()
            print('YOU WON!')
            print_seperator()

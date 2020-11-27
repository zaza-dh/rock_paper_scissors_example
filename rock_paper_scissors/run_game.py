import argparse
from rock_paper_scissors.game import RPSGame
from rock_paper_scissors.player import Player


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Play a game of Rock Paper Scissor. Press CTRL+C at any time to exit '
                                                 'the game')

    parser.add_argument('--number-of-rounds', type=int, default=None, required=False,
                        help='The number of rounds to be player.')
    parser.add_argument('--player-name', type=str, default=None, required=False,
                        help='The name/nickname you wish to give yourself in this game.')

    args = parser.parse_args()
    return args


def main():
    try:
        args = parse_cli_args()

        print('Welcome to the super game which is piere papier ciseau, prepare to be destroyed')
        player_one = Player(name='computer', human_player=False)

        if args.player_name:
            player_two_name = args.player_name
        else:
            player_two_name = input("Enter your name: ")

        player_two = Player(name=player_two_name, human_player=True)
        mon_jeu = RPSGame(player_one, player_two, args.number_of_rounds)

        mon_jeu.start_game()
    except KeyboardInterrupt:
        print("Exiting the game...")

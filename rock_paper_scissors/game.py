from rock_paper_scissors.graphical_helpers import plot_round_graphics


class RPSGame:
    def __init__(self, player_one, player_two, number_of_rounds):
        self.player_one = player_one
        self.player_two = player_two
        self.number_of_rounds = number_of_rounds

    @staticmethod
    def read_number_of_rounds():
        is_valid_input = False
        while not is_valid_input:
            user_given_number_of_rounds = input('For how many rounds do you want to play: ')
            try:
                number_of_rounds = int(user_given_number_of_rounds)
                is_valid_input = True
            except ValueError:
                print(f'please enter a number {user_given_number_of_rounds} cannot be accepted as a number:')
        return number_of_rounds

    def get_round_winner(self):
        if self.player_one.currently_played_hand > self.player_two.currently_played_hand:
            return self.player_one
        elif self.player_one.currently_played_hand < self.player_two.currently_played_hand:
            return self.player_two
        else:
            return None

    def start_round(self):
        self.player_one.play_round()
        self.player_two.play_round()

        print(f'{self.player_one.currently_played_hand.hand_type} VS {self.player_two.currently_played_hand.hand_type}')
        print(plot_round_graphics(self.player_one, self.player_two))
        winner = self.get_round_winner()
        if winner:
            winner.increment_score()
            print(f'the winner for this round is: {winner.player_name}')
        else:
            print('This round was a tie')

    def get_game_winner(self):
        """
        A function which determines who won the game.
        :return: The player who one the game, if the game resulted in a tie it will return `None`
        """
        if self.player_one.score > self.player_two.score:
            return self.player_one
        elif self.player_one.score < self.player_two.score:
            return self.player_two
        else:
            return None

    @staticmethod
    def print_end_of_game_message(game_winner):
        if not game_winner:
            print("well looks like no one won this time.")
        elif game_winner.human_player:
            print(f'well done {game_winner.player_name} you destroyed the computer')
        else:
            print(f'This time the machine won')

    def print_game_summary(self):
        print('Here is a summary of the game \n')
        print(f'{self.player_one.player_name} played ths hand: {self.player_one.played_hands}\n')
        print(f'{self.player_two.player_name} played this hand: {self.player_two.played_hands}\n')

    def start_game(self):
        if not self.number_of_rounds:
            self.number_of_rounds = self.read_number_of_rounds()
        current_round = 1
        while self.number_of_rounds >= current_round:
            print(f'Round number {self.number_of_rounds}')
            self.start_round()
            current_round += 1
        game_winner = self.get_game_winner()
        self.print_end_of_game_message(game_winner)
        self.print_game_summary()

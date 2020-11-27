import random

from rock_paper_scissors.constants import PLAYABLE_HANDS
from rock_paper_scissors.hand import Hand


class Player:
    def __init__(self, name, human_player):
        self.player_name = name
        self.played_hands = []
        self.score = 0
        self.human_player = human_player
        self.currently_played_hand = None

    @staticmethod
    def read_played_hand():
        currently_played_hand = input('what is your hand: ')
        if currently_played_hand.lower() in PLAYABLE_HANDS:
            return currently_played_hand.lower()
        print(f'you hand can only be one of the following options {PLAYABLE_HANDS}')
        return False

    def play_round(self):
        if self.human_player:
            is_valid_input = False
            while not is_valid_input:
                currently_played_hand = self.read_played_hand()
                if currently_played_hand:
                    is_valid_input = True
        else:
            currently_played_hand = random.choice(PLAYABLE_HANDS)

        self.store_played_hand(currently_played_hand)
        self.currently_played_hand = Hand(currently_played_hand)

    def increment_score(self):
        self.score += 1

    def store_played_hand(self, hand_type):
        self.played_hands.append(hand_type)

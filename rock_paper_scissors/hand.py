from rock_paper_scissors.constants import PAPER, ROCK, SCISSORS


class Hand:
    def __init__(self, hand_type):
        self.hand_type = hand_type

    def __eq__(self, other):
        return self.hand_type == other.hand_type

    def __gt__(self, other):
        if (self.hand_type == PAPER and other.hand_type == ROCK) or \
                (self.hand_type == ROCK and other.hand_type == SCISSORS) or (
                self.hand_type == SCISSORS and other.hand_type == PAPER):
            return True
        else:
            return False

    def __lt__(self, other):
        return other > self

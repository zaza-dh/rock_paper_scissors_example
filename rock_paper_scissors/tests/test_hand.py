import pytest

from rock_paper_scissors.constants import PAPER, ROCK, SCISSORS
from rock_paper_scissors.hand import Hand


class TestHand:

    @pytest.fixture()
    def other_hand(self):
        return Hand(SCISSORS)

    def test___eq__true(self, other_hand):
        my_hand = Hand(SCISSORS)
        result = my_hand.__eq__(other_hand)
        assert result is True

    def test___eq__false(self, other_hand):
        my_hand = Hand(ROCK)
        result = my_hand.__eq__(other_hand)
        assert result is False

    def test___gt__true(self, other_hand):
        my_hand = Hand(ROCK)
        result = my_hand.__gt__(other_hand)
        assert result is True

    def test___gt__false(self, other_hand):
        my_hand = Hand(PAPER)
        result = my_hand.__gt__(other_hand)
        assert result is False

    def test___lt__true(self, other_hand):
        my_hand = Hand(PAPER)
        result = my_hand.__lt__(other_hand)
        assert result is True

    def test___lt__false(self, other_hand):
        my_hand = Hand(ROCK)
        result = my_hand.__lt__(other_hand)
        assert result is False

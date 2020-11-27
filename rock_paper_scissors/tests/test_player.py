import pytest
from mock import patch

from rock_paper_scissors.player import Player


class TestPlayer:

    @pytest.fixture()
    def player_human(self):
        return Player('steve', True)

    @pytest.fixture()
    def player_non_human(self):
        return Player('player_computer', False)

    def test_player_human(self, player_human):
        assert player_human.human_player is True
        assert player_human.score == 0

    def test_player_non_human(self, player_non_human):
        assert player_non_human.human_player is False
        assert player_non_human.score == 0

    @patch('rock_paper_scissors.player.Player.read_played_hand')
    def test_play_round_human(self, mock_read_played_hand, player_human):
        mock_read_played_hand.return_value = 'rock'
        player_human.play_round()
        assert player_human.played_hands == ['rock']

    def test_play_round_non_human(self, player_non_human):
        with patch('random.choice', return_value='rock'):
            player_non_human.play_round()
            assert len(player_non_human.played_hands) > 0
            assert player_non_human.played_hands == ['rock']

    @patch('builtins.input', lambda *args: 'rock')
    def test_read_played_hand_good_answer(self, player_human):
        played_hand = player_human.read_played_hand()
        assert played_hand == 'rock'

    @patch('builtins.input', lambda *args: 'wrong_answer')
    def test_read_played_hand_bad_answer(self, player_human):
        played_hand = player_human.read_played_hand()
        assert played_hand is False

    def test_increment_score(self, player_human):
        assert player_human.score == 0
        player_human.increment_score()
        assert player_human.score == 1

    def test_store_played_hand(self, player_non_human):
        assert player_non_human.played_hands == []
        player_non_human.store_played_hand('rock')
        assert player_non_human.played_hands == ['rock']

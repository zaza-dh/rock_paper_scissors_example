from mock import MagicMock
import pytest

from rock_paper_scissors.game import RPSGame
from rock_paper_scissors.hand import Hand


@pytest.fixture()
def hand():
    hand = MagicMock()
    hand.return_value = 'rock'
    return hand


@pytest.fixture()
def mock_incre():
    mock_incre = MagicMock()
    mock_incre.return_value = None
    return mock_incre


@pytest.fixture()
def player_human_rock(hand, mock_incre):
    return MagicMock(player_name='steve',
                     played_hands=[],
                     score=1,
                     human_player=True,
                     currently_played_hand=Hand('rock'),
                     play_round=hand,
                     increment_score=mock_incre)


@pytest.fixture()
def player_human_scissors(hand, mock_incre):
    return MagicMock(player_name='stephan',
                     played_hands=[],
                     score=0,
                     human_player=True,
                     currently_played_hand=Hand('scissors'),
                     play_round=hand,
                     increment_score=mock_incre)


@pytest.fixture()
def player_non_human_scissors(hand, mock_incre):
    return MagicMock(player_name='computer',
                     played_hands=[],
                     score=0,
                     human_player=False,
                     currently_played_hand=Hand('scissors'),
                     increment_score=mock_incre,
                     play_round=hand)


@pytest.fixture()
def game_with_different_hands(player_human_rock, player_non_human_scissors):
    return RPSGame(player_human_rock, player_non_human_scissors, 1)


@pytest.fixture()
def game_with_different_hands_switched(player_human_rock, player_non_human_scissors):
    return RPSGame(player_non_human_scissors, player_human_rock, 1)


@pytest.fixture()
def game_with_similar_hands(player_human_scissors, player_non_human_scissors):
    return RPSGame(player_human_scissors, player_non_human_scissors, 1)

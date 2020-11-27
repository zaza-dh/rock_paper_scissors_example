from mock import patch


class TestRPSGame:

    def test_start_round_scoring(self, game_with_different_hands):
        game_with_different_hands.start_round()
        game_with_different_hands.player_one.play_round.assert_called()
        game_with_different_hands.player_two.play_round.assert_called()
        game_with_different_hands.player_two.increment_score.assert_called()

    def test_start_round_non_scoring(self, game_with_similar_hands):
        game_with_similar_hands.start_round()
        game_with_similar_hands.player_one.play_round.assert_called()
        game_with_similar_hands.player_two.play_round.assert_called()

    def test_get_game_winner_winner_one(self, game_with_different_hands):
        game_winner = game_with_different_hands.get_game_winner()
        assert game_winner.score == 1
        assert game_winner.player_name == 'steve'

    def test_get_game_winner_winner_two(self, game_with_different_hands_switched):
        game_winner = game_with_different_hands_switched.get_game_winner()
        assert game_winner.score == 1

    def test_get_game_winner_no_winner(self, game_with_similar_hands):
        game_winner = game_with_similar_hands.get_game_winner()
        assert game_winner is None

    def test_get_round_winner_winner_one(self, game_with_different_hands):
        round_winner = game_with_different_hands.get_round_winner()
        assert round_winner.player_name == 'steve'

    def test_get_round_winner_winner_two(self, game_with_different_hands_switched):
        round_winner = game_with_different_hands_switched.get_round_winner()
        assert round_winner.score == 1
        assert round_winner.player_name == 'steve'

    def test_get_round_winner_no_winner(self, game_with_similar_hands):
        round_winner = game_with_similar_hands.get_round_winner()
        assert round_winner is None

    @patch('builtins.print')
    def test_print_end_of_game_message_steve_won(self, mocked_print, game_with_similar_hands, player_human_rock):
        game_with_similar_hands.print_end_of_game_message(player_human_rock)
        mocked_print.assert_called_with('well done steve you destroyed the computer')

    @patch('builtins.print')
    def test_print_end_of_game_message_no_winner(self, mocked_print, game_with_similar_hands):
        game_with_similar_hands.print_end_of_game_message(None)
        mocked_print.assert_called_with('well looks like no one won this time.')

    @patch('builtins.print')
    def test_print_end_of_game_message_computer_won(self, mocked_print,
                                                    game_with_similar_hands, player_non_human_scissors):
        game_with_similar_hands.print_end_of_game_message(player_non_human_scissors)
        mocked_print.assert_called_with('This time the machine won')

    @patch('builtins.print')
    def test_print_game_summary(self, mocked_print, game_with_similar_hands):
        game_with_similar_hands.print_game_summary()
        assert 3 == mocked_print.call_count

    @patch('rock_paper_scissors.game.RPSGame.print_game_summary')
    @patch('rock_paper_scissors.game.RPSGame.print_end_of_game_message')
    @patch('rock_paper_scissors.game.RPSGame.get_game_winner')
    @patch('rock_paper_scissors.game.RPSGame.start_round')
    def test_start_game_with_number_of_rounds(self,
                                              mock_start_round,
                                              mock_get_game_winner,
                                              mock_print_end_of_game_message,
                                              mock_print_game_summary,
                                              game_with_similar_hands):
        game_with_similar_hands.number_of_rounds = 2
        game_with_similar_hands.start_game()
        assert 2 == mock_start_round.call_count
        mock_get_game_winner.assert_called_once()
        mock_print_end_of_game_message.assert_called_once()
        mock_print_game_summary.asser_called_once()

    @patch('rock_paper_scissors.game.RPSGame.print_game_summary')
    @patch('rock_paper_scissors.game.RPSGame.print_end_of_game_message')
    @patch('rock_paper_scissors.game.RPSGame.get_game_winner')
    @patch('rock_paper_scissors.game.RPSGame.read_number_of_rounds')
    def test_start_game_no_number_of_rounds(self,
                                            mock_read_number_of_rounds,
                                            mock_get_game_winner,
                                            mock_print_end_of_game_message,
                                            mock_print_game_summary,
                                            game_with_similar_hands):
        game_with_similar_hands.number_of_rounds = 0
        mock_read_number_of_rounds.return_value = 0
        game_with_similar_hands.start_game()
        mock_read_number_of_rounds.assert_called_once()
        mock_get_game_winner.assert_called_once()
        mock_print_end_of_game_message.assert_called_once()
        mock_print_game_summary.asser_called_once()

    @patch('builtins.input', lambda *args: '3')
    def test_read_number_of_rounds(self, game_with_similar_hands):
        number_of_rounds = game_with_similar_hands.read_number_of_rounds()
        assert number_of_rounds == 3

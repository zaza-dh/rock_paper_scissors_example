from rock_paper_scissors.graphical_helpers import (plot_round_graphics,
                                                  reverse_hand)


class TestGraphicalHelpers:

    def test_reverse_hand(self):
        original_string = " 12345"
        reversed_string = "54321 "
        assert reverse_hand(original_string) == reversed_string

    def test_reverse_hand_multiline(self):
        original_string = ("12345\n"
                           "678910")
        reversed_string = ("54321\n"
                           "019876")
        assert reverse_hand(original_string) == reversed_string

    def test_plot_round(self, player_human_rock, player_non_human_scissors):
        string = """steve                                computer
    ___                                       ___    
---'   __)                                 _(_   '---
     (___)                              (__          
      (___)                              (____       
      (__)                                 (__(      
---._(__)                                   (__(_.---
"""
        assert plot_round_graphics(player_human_rock, player_non_human_scissors) == string

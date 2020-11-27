from rock_paper_scissors.constants import PAPER, ROCK, SCISSORS

# Rock
rock_art = ("    ___             \n"
            "---'   __)          \n"
            "     (___)          \n"
            "      (___)         \n"
            "      (__)          \n"
            "---._(__)           ")
# Paper
paper_art = ("     ___           \n"
             "---'    _)_        \n"
             "           __)     \n"
             "          ___)     \n"
             "         ___)      \n"
             "---.____)          ")
# Scissors
scissorss_art = ("    ___              \n"
                "---'   _)_           \n"
                "          __)        \n"
                "       ____)         \n"
                "      (__)           \n"
                "---._(__)            ")

hand_name_to_ascii_art = {ROCK: rock_art, PAPER: paper_art, SCISSORS: scissors_art}


def reverse_hand(hand_ascii):
    new_lines = []
    for line in hand_ascii.split("\n"):

        new_line = line[::-1]
        new_line = new_line.replace("(", ")")
        new_line = new_line.replace(")", "(")
        new_lines.append(new_line)
    reversed_hand = "\n".join(new_lines)
    return reversed_hand


def plot_round_graphics(player1, player2):
    hand1_art = hand_name_to_ascii_art[player1.currently_played_hand.hand_type]
    hand2_art = hand_name_to_ascii_art[player2.currently_played_hand.hand_type]
    hand2_art = reverse_hand(hand2_art)
    round_plot = player1.player_name + " " * 32 + player2.player_name + "\n"
    for line1, line2 in zip(hand1_art.split("\n"), hand2_art.split("\n")):
        round_line = line1 + " " * 12 + line2 + "\n"
        round_plot += round_line
    return round_plot

import io, sys
from app.game.player import Player

def test_get_hand():
    """
    Test the get_hand method of the Player class.
    """
    player = Player("TestPlayer")
    player.hand = ["Card1", "Card2"]  # Manually setting the hand for testing

    assert player.get_hand() == ["Card1", "Card2"]


def test_player_repr():
    """
    Test the __repr__ method of the Player class.
    """
    player = Player("TestPlayer")
    player.hand = ["Card1", "Card2"]  # Manually setting the hand for testing

    # Check if the string representation is correct
    assert str(player) == "TestPlayer: ['Card1', 'Card2']"

def test_do_action():
    """
    Test the do_action method of the Player class.
    This method prints to the console, so we will check if it prints the expected output.
    """

    player = Player("TestPlayer")

    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the method
    player.do_action("check")

    # Reset redirect.
    sys.stdout = sys.__stdout__

    # Check if the output is as expected                  
    assert captured_output.getvalue().strip() == "TestPlayer performs action: check"
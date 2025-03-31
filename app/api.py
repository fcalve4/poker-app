import sys, io

from fastapi import APIRouter
from app.game.game import PokerGame
from app.game.table import PokerTable
router = APIRouter()

@router.get("/")
def root():
    # Create a new Pokertable with a capacity of 6 players
    table = PokerTable(6)

    # Add players to the table manually for now
    table.add_player("Sonny")
    table.add_player("Fredo")
    table.add_player("Michael")

    print("DEBUGGING - PRINTING PLAYERs -> ", str(table.get_players()))

    # Create a PokerGame instance with the table of players
    game = PokerGame(table)

    # Redirect stdout to capture print statements
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Play a hand of poker with the number of players dealt in
    game.game_loop()

    # Reset redirect.
    sys.stdout = sys.__stdout__

    # Return the captured output for debugging purposes
    # This will return the output of the game loop to the API response
    return {
        "message": "Poker game simulation completed.",
        "output": captured_output.getvalue()
    }
    


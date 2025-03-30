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


    # Play a hand of poker with the number of players dealt in
    game.game_loop()


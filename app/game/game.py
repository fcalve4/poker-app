from app.game.player import Player
from app.game.deck import Deck


class PokerGame():

    def __init__(self):
        """
        Initialize the PokerGame instance.
        This will set up the game state, including the deck and players.
        """
        pass

    def deal_initial_hand(self):
        deck = Deck()
        deck.shuffle_deck()

        players = [Player("Fredo"), Player("Michael")]
        for player in players:
            player.hand = [deck.draw_card(), deck.draw_card()]
        
        return {p.name: p.hand for p in players}

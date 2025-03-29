from app.game.deck import create_deck, shuffle_deck
from app.game.player import Player

def run_poker_round():
    deck = create_deck()
    shuffle_deck(deck)

    players = [Player("Alice"), Player("Bob")]
    for player in players:
        player.hand = [deck.pop(), deck.pop()]

    return {p.name: p.hand for p in players}

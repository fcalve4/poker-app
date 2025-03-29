import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def create_deck():
    return [rank + suit for suit in SUITS for rank in RANKS]

def shuffle_deck(deck):
    random.shuffle(deck)

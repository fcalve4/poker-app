class Card():
    """
    Represents a single playing card with a suit and a rank.
    """

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
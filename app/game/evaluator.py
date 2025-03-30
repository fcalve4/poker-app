class Evaluator():
    """
    This class is responsible for evaluating the game state.
    It will determine which player has the best hand."""

    def __init__(self):
        """
        Initialize the Evaluator class.
        """
        pass
    
    def evaluate(self, players, community_cards):
        """
        Evaluate the poker hands and determine the best hand.
        :param hands: A dictionary where keys are player names and values are their respective hands.
        :return: The player with the best hand and their hand ranking.
        """
        # Evaluate each player's hand against poker hand rankings
        best_player = None
        best_hand = None
        
        # For now, just return the first player as the winner for demonstration purposes
        for player in players:
            hand = player.get_hand()
            print(f"Evaluating {player}'s hand: {hand}")
            best_player = player
            best_hand = hand
            break # For now break and return fist player
        
        return best_player, best_hand
    

    def is_flush_possible(self, community_cards):
        """
        Check if a flush is possible with the given community cards.
        :param community_cards: List of community cards.
        :return: True if a flush is possible, False otherwise.
        """
        # Check for flush possibilities
        suits = [card.suit for card in community_cards]
        suit_count = {suit: suits.count(suit) for suit in set(suits)}
        
        # A flush is possible if there are 3 or more cards of the same suit on the board
        for count in suit_count.values():
            if count >= 3:
                return True
        return False

    def is_board_paired(self, community_cards):
        """
        Check if the community cards are paired.
        :param community_cards: List of community cards.
        :return: True if there is a pair on the board, False otherwise.
        """
        # Check for pairs on the board
        ranks = [card.rank for card in community_cards]
        rank_count = {rank: ranks.count(rank) for rank in set(ranks)}
        
        # A pair exists if any rank appears at least twice
        for count in rank_count.values():
            if count >= 2:
                return True
        return False
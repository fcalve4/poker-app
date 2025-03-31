import itertools

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

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
        
        for player in players:
            hand = player.get_hand()
            print(f"Evaluating {player}'s hand: {hand}")
            best_player = player
            best_hand = hand
        
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
    


    def get_list_of_possible_hands(self, player_hand, community_cards):
        """
        Determine all possible hands a player can make with their hand and the community cards.
        :param player_hand: The player's hand (list of card objects).
        :param community_cards: List of community cards.
        :return: A list of possible hands (list of lists) that can be formed.
        """
        possible_five_card_hands = []

        available_cards = player_hand + community_cards
        
        possible_five_card_hands = list(itertools.combinations(available_cards, 5))
        
        return possible_five_card_hands

    def get_best_hand(self, possible_hands):
        """
        Determine the best hand from a list of possible hands.
        :param possible_hands: A list of possible 5 card hands.
        :return: The best hand based on poker hand rankings.
        """
        for hand in possible_hands:
            pass

    def check_for_straight(self, hand):
        """
        Check if the given hand is a straight.
        :param hand: A list of card objects representing a 5-card hand.
        :return: True if the hand is a straight, False otherwise.
        """
        # Sort the hand by rank
        sorted_hand = sorted(hand, key=lambda x: x.rank)
        
        # Extract ranks and convert to indices
        ranks = [card.rank for card in sorted_hand]
        rank_indices = [RANKS.index(rank) for rank in ranks]
        
        # Check for consecutive ranks
        if all(rank_indices[i] + 1 == rank_indices[i + 1] for i in range(len(rank_indices) - 1)):
            return True
        return False

    def check_for_flush(self, hand):
        """
        Check if the given hand is a flush.
        :param hand: A list of card objects representing a 5-card hand.
        :return: True if the hand is a flush, False otherwise.
        """
        # Check if all cards in the hand have the same suit
        suits = [card.suit for card in hand]
        
        # A flush occurs if all cards have the same suit
        if len(set(suits)) == 1:
            return True
        return False
        

    def check_for_straightflush(self, hand):
        """
        Check if the given hand is a straight flush.
        :param hand: A list of card objects representing a 5-card hand.
        :return: True if the hand is a straight flush, False otherwise.
        """
        # First check for flush
        if not self.check_for_flush(hand):
            return False
        
        # Then check for straight
        if self.check_for_straight(hand):
            return True
        
        return False




from app.game.player import Player
from app.game.deck import Deck


class PokerGame():

    def __init__(self, table):
        """
        Initialize the PokerGame instance.
        This will set up the game state, including the deck and players.
        """
        self.table = table
        self.community_cards = []
        # Create and shuffle a new deck
        self.deck = Deck()

        # Initliaze the player in seat 0 to be the first dealer
        self.table.get_players()[0].is_dealer = True  # Set the first player as dealer
        # Note: In a real game, the dealer would rotate after each hand.
        # Will need to implement this later on
        


    
    def deal_initial_hand(self):
        self.deck.shuffle_deck()

        # For every player on the table, add 2 cards to their hand
        for player in self.table.get_players():
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
    

    def play_preflop_betting_round(self, num_players_in_hand):
        # Player in the seat left of the dealer posts SMALL BLIND
        # Player in the seat left of the dealer posts BIG BLIND

        # Action starts on UTG, so if the dealer is in seat 0, the action will start on seat 2
        is_action_open = True
        while is_action_open:
            # Loop through each player in the table to perform actions
            for i in range(len(self.table.get_players())):
                player_index = (i + 1) % len(self.table.get_players())
                player = self.table.get_players()[player_index]
                player.do_action("check")

            is_action_open = False

    def deal_flop(self):
        """
        Deal the flop (3 community cards).
        In a real game, this would involve drawing cards from the deck and placing them on the table.
        """
        # Placeholder for dealing flop logic
        # In a real implementation, you'd draw 3 cards from the deck and place them on the table
        self.community_cards.append(self.deck.draw_card())
        self.community_cards.append(self.deck.draw_card())
        self.community_cards.append(self.deck.draw_card())
        print(f"Dealing Flop: ", self.community_cards[0].__repr__(), self.community_cards[1].__repr__(), self.community_cards[2].__repr__())
        


    def play_hand(self, num_players_dealt_in):
        self.deal_initial_hand
        self.play_preflop_betting_round(num_players_dealt_in)
        self.deal_flop()
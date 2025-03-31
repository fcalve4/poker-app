from app.game.player import Player
from app.game.deck import Deck
from app.game.deck import Card
from app.game.evaluator import Evaluator


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
        self.deck.shuffle_deck()

        # Initliaze the player in seat 0 to be the first dealer
        self.table.get_players()[0].is_dealer = True  # Set the first player as dealer
        # Note: In a real game, the dealer would rotate after each hand.
        # Will need to implement this later on
        
        self.hand_evaluator = Evaluator()  # Initialize the hand evaluator


    
    def deal_initial_hand(self):
        # For every player on the table, add 2 cards to their hand
        for player in self.table.get_players():
            player.hand = [self.deck.draw_card(), self.deck.draw_card()]
    

    def play_preflop_betting_round(self):
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

    def deal_community_card(self):
        """
        Deal the flop (3 community cards).
        In a real game, this would involve drawing cards from the deck and placing them on the table.
        """
        # Placeholder for dealing flop logic
        # In a real implementation, you'd draw 3 cards from the deck and place them on the table
        card = self.deck.draw_card()
        self.community_cards.append(card)
        print(f"Dealing card: ", card.__repr__())
        
    
    def play_standard_betting_round(self):
        """
        Play the betting round after the flop is dealt.
        This would involve each player taking turns to act based on the community cards.
        """
        # Placeholder for flop betting logic
        # In a real implementation, you'd loop through players and let them take actions based on the community cards
        is_action_open = True
        while is_action_open:
            for i in range(len(self.table.get_players())):
                player_index = (i + 1) % len(self.table.get_players())
                player = self.table.get_players()[player_index]
                player.do_action("check")

            is_action_open = False


    def play_hand(self):
        # Perform initial deal
        self.deal_initial_hand()
        # Play the preflop betting round
        self.play_preflop_betting_round()
        print("-------------- DEALING FLOP ------------------")
        # Deal the flop (3 community cards)
        self.deal_community_card()
        self.deal_community_card()
        self.deal_community_card()
        # After dealing the flop, play the standard betting round (FLOP)
        self.play_standard_betting_round()

        print("-------------- DEALING TURN ------------------")
        # Deal the TURN
        self.deal_community_card()

        # After dealing the turn, play the standard betting round (TURN)
        self.play_standard_betting_round()

        # Deal the RIVER
        print("-------------- DEALING RIVER ------------------")
        self.deal_community_card()

        # After dealing the river, play the standard betting round (RIVER)
        self.play_standard_betting_round()

        # Evaluate the final hands and determine the winner
        self.hand_evaluator.evaluate(self.table.get_players(), self.community_cards)


    def game_loop(self):
        """
        Main game loop to handle the flow of the poker game.
        """
        # This function can be used to manage the overall game loop
        # For now, it will just call play_hand() to simulate a single hand of poker
        for i in range(1):
            self.play_hand()
    

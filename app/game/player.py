class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.is_dealer = False # False by default, determined at the start of hand


    def do_action(self, action):
        """
        Perform an action in the game.
        :param action: The action to be performed (ex. fold, call, raise).
        :return: None
        """
        print(f"{self.name} performs action: {action}")

    def get_hand(self):
        """
        Get the player's hand.
        :return: The player's hand (list of card objects).
        """
        return self.hand

    def __repr__(self):
        return f"{self.name}: {self.hand}"

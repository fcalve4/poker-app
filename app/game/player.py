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

    def __repr__(self):
        return f"{self.name}: {self.hand}"

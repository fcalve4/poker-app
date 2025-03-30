from app.game.player import Player
from app.game.deck import Deck


class PokerTable():

    def __init__(self, total_num_seats):
        self.total_num_seats = total_num_seats
        self.players = []

    
    def add_player(self, player_name):
        """
        Adds a player to the table if there is an available seat.
        :param player_name: Name of the player to be added.
        :return: True if player was added, False if no seats are available.
        """
        if len(self.players) < self.total_num_seats:
            new_player = Player(player_name)
            self.players.append(new_player)
            return True
        else:
            return False
        

    
from app.game.player import Player
from app.game.deck import Deck


class PokerTable():
    """
    PokerTable is a container for the player objects that are in the game. Real implementation will have
    Multiple tables for multiple games.
    """

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
        
    def remove_player(self, player_name):
        """
        Removes a player from the table.
        :param player_name: Name of the player to be removed.
        :return: True if player was removed, False if the player was not found.
        """
        for i, player in enumerate(self.players):
            if player.name == player_name:
                del self.players[i]
                return True
        return False
    
    def get_players(self):
        """
        Returns a list of players currently at the table.
        :return: List of Player objects at the table.
        """
        return self.players
        

    
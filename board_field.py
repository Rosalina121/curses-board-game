# board field class that contains: game: a char where default is "O", players: a mutable set of players from Player class
from player import Player


class BoardField:
    def __init__(self, game, players):
        self.game = game

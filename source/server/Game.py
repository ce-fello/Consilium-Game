import Map
import Player


class Game:
    def __init__(self, players: [Player], map: Map):
        self.players = players
        self.map = map

    def __str__(self):
        return f"PLAYERS: {self.players} MAP: {self.map}"

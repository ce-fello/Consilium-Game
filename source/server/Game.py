from source.server.Player import Player
from source.server.Map import Map


class Game:
    def __init__(self, players: [Player], map: Map):
        self.players = players
        self.map = map

    def __str__(self):
        return f"PLAYERS: {self.players} MAP: {self.map.__str__()}"

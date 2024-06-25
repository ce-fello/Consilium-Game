from source.server.Player import Player
from source.server.Map import Map
from source.server.Time import Time


class Game:
    def __init__(self, players: [Player], map: Map, time: Time):
        self.players = players
        self.map = map
        self.time = time

    def __str__(self):
        return f"PLAYERS: {self.players} MAP: {self.map.__str__()}"

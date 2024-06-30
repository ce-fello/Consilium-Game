from source.server.Player import Player
from source.server.Map import Map
from source.server.Time import Time
from source.server.Decision import Decision
from os import listdir
from os.path import isfile, join

class Game:
    def __init__(self, players: [Player], map: Map, time: Time):
        self.players = players
        self.map = map
        self.time = time
        self.politic_decisions = self.load_decisions('politics')
        self.economic_decisions = self.load_decisions('economics')

    def load_decisions(self, kind):
        decisions = []
        route = f"../resources/decisions/{kind}/"
        decisions_names = [f for f in listdir(route) if isfile(join(route, f))]
        for i in decisions_names:
            decisions.append(Decision(route + i))
        return decisions


    def __str__(self):
        return f"PLAYERS: {self.players} MAP: {self.map.__str__()}"



class ClientPacket:
    def __init__(self, name, decisions=None):
        self.name = name
        self.decisions = decisions


class ServerPacket:
    def __init__(self, name, players=None):
        self.name = name
        if players:
            self.players = players
        else:
            self.players = []


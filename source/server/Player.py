from source.server.Economics import Economics


class Player:
    def __init__(self, id: int, name: str, stability: int, economics: Economics):
        self.id = id
        self.name = name
        self.stability = stability
        self.economics = economics
        self.available_politic_decisions = True
        self.available_economic_decisions = True

    def __str__(self):
        return f"ID: {self.id} NAME: {self.name} ECONOMICS {self.economics}"

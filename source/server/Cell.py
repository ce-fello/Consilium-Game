class Cell:
    def __init__(self, id: int, type: str, neighbours: list, owner: int):
        self.id = id
        self.type = type
        self.neighbours = neighbours
        self.owner = owner

    def __str__(self):
        return f"{self.id} {self.type} {self.neighbours} {self.owner}"

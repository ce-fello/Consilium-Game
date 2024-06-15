import Cell


class Map:
    def __init__(self, cells: [Cell]):
        self.cells = cells

    def __str__(self):
        return f"CELLS: {self.cells}"

from source.server.Cell import Cell
from source.server.Map import Map


def parse_cells_from_file(path: str):
    file = open(path)
    lines = [i for i in file]
    cells = []
    for s in lines:
        args = s.split(';')
        id = int(args[0])
        cell_type = args[1]
        neighbours = []
        owner = args[-1]
        for x in range(2, len(args) - 1):
            neighbours.append(args[x])
        cell = Cell(id, cell_type, neighbours, owner)
        cells.append(cell)
    return cells


def create_map(path: str):
    return Map(parse_cells_from_file(path))

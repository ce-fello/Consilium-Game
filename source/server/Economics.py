from source.server.Sector import Sector


class Economics:
    def __init__(self, owner: int, sectors: [Sector]):
        self.owner = owner
        self.sectors = sectors

    def __str__(self):
        return f"OWNER: {self.owner} SECTORS: {self.sectors}"

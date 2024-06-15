import Economics


class State:
    def __init__(self, head: int, name: str, territory: list, economics: Economics, gdp: int, population: int,
                 current_effects: list):
        self.head = head
        self.name = name
        self.territory = territory
        self.economics = economics
        self.gdp = gdp
        self.population = population
        self.current_effects = current_effects

    def __str__(self):
        return (f"HEAD: {self.head} NAME: {self.name} TERRITORY: {self.territory} ECONOMICS: {self.economics} "
                f"GDP: {self.gdp} POPULATION: {self.population}")

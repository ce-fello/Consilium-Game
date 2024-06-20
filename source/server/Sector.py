class Sector:
    def __init__(self, name: str, value: int, k_buff: float, k_debuff: float):
        self.name = name
        self.value = value
        self.k_buff = k_buff
        self.k_debuff = k_debuff
        self.proportion = 0

    def __str__(self):
        return f"NAME: {self.name} VALUE: {self.value} K_BUFF: {self.k_buff} K_DEBUFF: {self.k_debuff}"

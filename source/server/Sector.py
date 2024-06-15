class Sector:
    def __init__(self, name: str, k_buff: float, k_debuff: float):
        self.name = name
        self.k_buff = k_buff
        self.k_debuff = k_debuff

    def __str__(self):
        return f"NAME: {self.name} K_BUFF: {self.k_buff} K_DEBUFF: {self.k_debuff}"

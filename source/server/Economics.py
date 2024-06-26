from source.server.Sector import Sector


class Economics:
    def __init__(self, sectors_value: [int], sectors_k_buff: [int], sectors_k_debuff: [int]):
        self.sectors_name = ['services', 'industry', 'education', 'healthcare', 'military', 'resources']
        self.sectors_name_ru = ['Сфера услуг', 'Промышленность', 'Образование', 'Здравоохранение',
                                'Военные расходы', 'Ресурсы']
        self.sectors_codes = ['🛒', '🔨', '📚', '⛑', '💀', '💎']
        self.sectors = {}
        self.capacity = sum(sectors_value)
        for i in range(len(self.sectors_name)):
            sector = Sector(self.sectors_name[i], sectors_value[i], sectors_k_buff[i],
                            sectors_k_debuff[i])
            sector.proportion = round(sector.value / self.capacity, 3) * 100
            self.sectors[self.sectors_name[i]] = Sector(self.sectors_name[i], sectors_value[i], sectors_k_buff[i],
                                                        sectors_k_debuff[i])

    def __str__(self):
        return f"SECTORS: {self.sectors}"

    def update_sectors(self):
        for i in range(len(self.sectors_name)):
            sector = self.sectors[self.sectors_name[i]]
            sector.value += round((sector.k_buff + (1 - sector.k_debuff)) / 10, 2)
        for i in range(len(self.sectors_name)):
            sector = self.sectors[self.sectors_name[i]]
            sector.value = round(sector.value, 2)

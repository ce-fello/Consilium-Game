from source.server.Sector import Sector


class Economics:
    def __init__(self, sectors_value: [int], sectors_k_buff: [int], sectors_k_debuff: [int]):
        self.sectors_name = ['services', 'industry', 'education', 'healthcare', 'military', 'resources']
        self.sectors_name_ru = ['Сфера услуг', 'Промышленность', 'Образование', 'Здравоохранение',
                                'Военные расходы', 'Ресурсы']
        self.sectors = {}
        for i in range(len(self.sectors_name)):
            self.sectors[self.sectors_name[i]] = Sector(self.sectors_name[i], sectors_value[i], sectors_k_buff[i],
                                                        sectors_k_debuff[i])

    def __str__(self):
        return f"SECTORS: {self.sectors}"

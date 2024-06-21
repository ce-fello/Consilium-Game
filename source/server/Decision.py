import json
from source.server.Player import Player


class Decision:
    def __init__(self, path, player: Player):
        self.sectors_name = ['services', 'industry', 'education', 'healthcare', 'military', 'resources']
        self.sectors_name_ru = ['Сфера услуг', 'Промышленность', 'Образование', 'Здравоохранение',
                                'Военные расходы', 'Ресурсы']
        self.sectors_codes = ['🛒', '🔨', '📚', '⛑', '💀', '💎']
        self.data = json.load(open(path, 'r', encoding='utf-8'))
        self.name = self.data['name']
        self.name_ru = self.data['name_ru']
        self.player = player
        self.tooltip = self.create_tooltip()

    def __str__(self):
        return f"NAME {self.name} NAME_RU {self.name_ru}"

    def available(self):
        stability_condition = self.data["conditions"][0]
        if stability_condition['value'] != '':
            if stability_condition['value'][0] == '>':
                if self.player.stability <= float(stability_condition['value'][1:]):
                    return False
            else:
                if self.player.stability >= float(stability_condition['value'][1:]):
                    return False
        for i in self.data["conditions"][1:]:
            if i["value"] != "":
                if i["value"][0] == ">":
                    if self.player.economics.sectors[i["sector"]].value <= float(i["value"][1:]):
                        return False
                else:
                    if self.player.economics.sectors[i["sector"]].value >= float(i["value"][1:]):
                        return False
            if i["k_buff"] != "":
                if i["k_buff"][0] == ">":
                    if self.player.economics.sectors[i["sector"]].k_buff <= float(i["k_buff"][1:]):
                        return False
                else:
                    if self.player.economics.sectors[i["sector"]].k_buff >= float(i["k_buff"][1:]):
                        return False
            if i["k_debuff"] != "":
                if i["k_debuff"][0] == ">":
                    if self.player.economics.sectors[i["sector"]].k_debuff <= float(i["k_debuff"][1:]):
                        return False
                else:
                    if self.player.economics.sectors[i["sector"]].k_debuff >= float(i["k_debuff"][1:]):
                        return False
        return True

    def apply(self):
        if self.available():
            stability_consequences = self.data["consequences"][0]
            if stability_consequences['value'] != 0:
                self.player.stability += stability_consequences['value']
            for i in self.data["consequences"][1:]:
                sector = self.player.economics.sectors[i["sector"]]
                if i["value"] > 0:
                    sector.value += i["value"] * sector.k_buff
                else:
                    sector.value += i["value"] * sector.k_debuff
                sector.k_buff += float(i["k_buff"])
                sector.k_debuff += float(i["k_debuff"])
                sector.value = round(sector.value, 2)
                sector.k_buff = round(sector.k_buff, 2)
                sector.k_debuff = round(sector.k_debuff, 2)

    def create_tooltip(self):
        text_tooltip = 'Условия\n'
        stability_condition = self.data['conditions'][0]
        if stability_condition['value'] != "":
            text_tooltip += f' {stability_condition["sector_code"]}   {stability_condition["value"]}\n'
            text_tooltip += '---------\n'
        for i in self.data["conditions"][1:]:
            if i["value"] != "":
                text_tooltip += f' {i["sector_code"]}   {i["value"]}\n'
            if i["k_buff"] != "":
                text_tooltip += f' {i["sector_code"]}⌃ {i["k_buff"]}\n'
            if i["k_buff"] != "":
                text_tooltip += f' {i["sector_code"]}⌄ {i["k_debuff"]}\n'
            text_tooltip += '---------\n'
        text_tooltip += 'Изменения\n'
        stability_change = self.data['consequences'][0]
        if stability_change['value'] > 0:
            text_tooltip += f' {stability_change["sector_code"]}   +{stability_change["value"]}\n'
            text_tooltip += '---------\n'
        elif stability_change['value'] < 0:
            text_tooltip += f' {stability_change["sector_code"]}   {stability_change["value"]}\n'
            text_tooltip += '---------\n'
        for i in self.data["consequences"][1:]:
            if i["value"] != 0:
                if i['value'] > 0:
                    text_tooltip += f' {i["sector_code"]}   +{i["value"]}\n'
                else:
                    text_tooltip += f' {i["sector_code"]}   {i["value"]}\n'
            if i["k_buff"] != 0:
                if i['k_buff'] > 0:
                    text_tooltip += f' {i["sector_code"]}⌃ +{i["k_buff"]}\n'
                else:
                    text_tooltip += f' {i["sector_code"]}⌃ {i["k_buff"]}\n'
            if i["k_buff"] != 0:
                if i['k_debuff'] > 0:
                    text_tooltip += f' {i["sector_code"]}⌄ +{i["k_debuff"]}\n'
                else:
                    text_tooltip += f' {i["sector_code"]}⌄ {i["k_debuff"]}\n'
            text_tooltip += '---------\n'

        return text_tooltip


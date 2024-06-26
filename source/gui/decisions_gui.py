from customtkinter import *
from source.server.Decision import Decision
from source.server.Player import Player
from source.server.Game import Game
from tkinter import *
from os import listdir
from os.path import isfile, join
from standard_gui import StandardFunctions


class DecisionsGUI:
    def __init__(self, root, canvas: Canvas, game: Game, player: Player):
        self.reference_data = []
        self.reference_decisions = []
        self.root = root
        self.canvas = canvas
        self.game = game
        self.player = player
        self.type_of_reference_data = 1
        self.standard = StandardFunctions(self.root)
        self.canvas.create_window(1540, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.economic_button())
        self.canvas.create_window(1650, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.politic_button())
        self.canvas.create_window(1430, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.government_button())

    def destroy_reference_data(self):
        if len(self.reference_data) != 0:
            for i in self.reference_data:
                i.destroy()
            self.reference_data = []

    def economic_button(self):
        photo = PhotoImage(file='../resources/images/economic_icon.png')
        press = self.standard.create_nice_button('', self.show_economics_decisions, photo, 80, 80)
        self.standard.tooltip(press, 'Экономические решения')
        return press

    def show_economics_decisions(self):
        self.type_of_reference_data = 2
        self.destroy_reference_data()
        self.reference_decisions = []
        
        route = "../resources/decisions/economics/"
        self.reference_data.append(self.standard.create_nice_label('Экономические решения', 40, 320))
        self.reference_decisions.append('Title')
        
        decisions_names = [f for f in listdir(route) if isfile(join(route, f))]
        for i in decisions_names:
            decision = Decision(route + i, self.player, self.game, 'economic')
            decision_button = self.standard.create_nice_button(decision.name_ru, decision.apply, None, 40, 400, 18)
            if not decision.available() or not self.game.available_economic_decisions:
                decision_button.configure(text_color='#464646')
            self.standard.tooltip(decision_button, decision.tooltip, False, 14)
            self.reference_data.append(decision_button)
            self.reference_decisions.append(decision)
            
        self.canvas.create_window(1390, 120, anchor="nw", window=self.reference_data[0])
        
        for i in range(1, len(self.reference_data)):
            self.canvas.create_window(1300, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def politic_button(self):
        photo = PhotoImage(file='../resources/images/politic_icon.png')
        press = self.standard.create_nice_button('', self.show_politic_decisions, photo, 80, 80)
        self.standard.tooltip(press, 'Политические решения')
        return press

    def show_politic_decisions(self):
        self.type_of_reference_data = 3
        self.destroy_reference_data()
        self.reference_decisions = []
        
        route = "../resources/decisions/politics/"
        self.reference_data.append(self.standard.create_nice_label('Политическое решения', 40, 320))
        self.reference_decisions.append('Title')
        
        decisions_names = [f for f in listdir(route) if isfile(join(route, f))]
        for i in decisions_names:
            decision = Decision(route + i, self.player, self.game, 'politic')
            decision_button = self.standard.create_nice_button(decision.name_ru, decision.apply, None, 40, 400, 18)
            if not decision.available() or not self.game.available_politic_decisions:
                decision_button.configure(text_color='#464646')
            self.standard.tooltip(decision_button, decision.tooltip, False, 14)
            self.reference_data.append(decision_button)
            self.reference_decisions.append(decision)
            
        self.canvas.create_window(1390, 120, anchor="nw", window=self.reference_data[0])
        
        for i in range(1, len(self.reference_data)):
            self.canvas.create_window(1300, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def government_button(self):
        photo = PhotoImage(file='../resources/images/state_icon.png')
        press = self.standard.create_nice_button('', self.show_government_information, photo, 80, 80)
        self.show_government_information()
        self.standard.tooltip(press, "Информация о государстве")
        return press

    def show_government_information(self):
        self.type_of_reference_data = 1
        self.destroy_reference_data()
        
        economics = self.player.economics
        self.update_proportions()
        self.reference_data.append(self.standard.create_nice_label('Информация о государстве', 40, 420))
        self.reference_data.append(self.standard.create_nice_label('Имя : ' + self.player.name, 40, 310))
        self.reference_data.append(self.standard.create_nice_label('⚖Стабильность ' +
                                                                             str(self.player.stability) + '%', 40, 310))
        for i in range(len(economics.sectors_name_ru)):
            sector = economics.sectors[economics.sectors_name[i]]
            self.reference_data.append(self.standard.create_nice_label(economics.sectors_codes[i] +
                                                              economics.sectors_name_ru[i], 40, 250))
            
            value = self.standard.create_nice_button(str(sector.value) + "💰", None, None, 40, 50, 18)
            proportion = self.standard.create_nice_button(str(sector.proportion) + '%', None, None, 40, 50, 18)
            tooltip_text = str(sector.k_buff) + ' ⌃\n' + \
                           str(sector.k_debuff) + ' ⌄'
            
            self.standard.tooltip(value, tooltip_text, False)
            self.reference_data.append(proportion)
            self.reference_data.append(value)
            
        self.canvas.create_window(1400, 120, anchor="nw", window=self.reference_data[0])
        self.canvas.create_window(1450, 170, anchor="nw", window=self.reference_data[1])
        self.canvas.create_window(1450, 220, anchor="nw", window=self.reference_data[2])
        for i in range(3, len(self.reference_data), 3):
            self.canvas.create_window(1400, 270 + (i - 3) / 3 * 50, anchor="nw", window=self.reference_data[i])
            self.canvas.create_window(1660, 270 + (i - 3) / 3 * 50, anchor="nw", window=self.reference_data[i + 1])
            self.canvas.create_window(1740, 270 + (i - 3) / 3 * 50, anchor="nw", window=self.reference_data[i + 2])

    def update_proportions(self):
        economics = self.player.economics
        capacity = 0
        for i in range(len(economics.sectors_name_ru)):
            sector = economics.sectors[economics.sectors_name[i]]
            capacity += sector.value
        for i in range(len(economics.sectors_name_ru)):
            sector = economics.sectors[economics.sectors_name[i]]
            sector.proportion = round(round(sector.value / capacity, 4) * 100, 2)
        economics.capacity = capacity

    def update_reference_data(self):
        if self.type_of_reference_data == 1:
            self.update_proportions()
            economics = self.player.economics
            if self.game.time.update_sectors:
                economics.update_sectors()
                self.game.time.update_sectors = False
            for i in range(3, len(self.reference_data), 3):
                new_proportion = str(economics.sectors[economics.sectors_name[int(i / 3 - 1)]].proportion) + '%'
                new_value = str(economics.sectors[economics.sectors_name[int(i / 3 - 1)]].value) + '💰'
                self.reference_data[i + 1].configure(text=new_proportion)
                self.reference_data[i + 2].configure(text=new_value)
        elif self.type_of_reference_data == 2:
            if self.game.time.update_decisions:
                self.game.available_economic_decisions = True
                self.game.available_politic_decisions = True
                self.game.time.update_decisions = False
            for i in range(1, len(self.reference_data)):
                if not self.reference_decisions[i].available() or not self.game.available_economic_decisions:
                    self.reference_data[i].configure(text_color='#464646')
                else:
                    self.reference_data[i].configure(text_color='white')
        elif self.type_of_reference_data == 3:
            if self.game.time.update_decisions:
                self.game.available_politic_decisions = True
                self.game.available_economic_decisions = True
                self.game.time.update_decisions = False
            for i in range(1, len(self.reference_data)):
                if not self.reference_decisions[i].available() or not self.game.available_politic_decisions:
                    self.reference_data[i].configure(text_color='#464646')
                else:
                    self.reference_data[i].configure(text_color='white')





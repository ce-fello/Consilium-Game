from customtkinter import *
from source.server.Decision import Decision
from tkinter import *


class DecisionsGUI:
    def __init__(self, root, canvas, player):
        self.reference_data = []
        self.root = root
        self.canvas = canvas
        self.player = player

    def pop_tooltip(self, wdgt, txt, view=True, font=10):
        pop = Toplevel(wdgt)
        pop.overrideredirect(True)
        Label(pop, text=txt, font=('Bookman Old Style', font), bg='#ECE2AE', borderwidth=2).pack()
        wdgt.bind('<Leave>', lambda x: pop.destroy())
        if view:
            x_center = wdgt.winfo_rootx() - 20
            y_center = wdgt.winfo_rooty() + wdgt.winfo_height() + 5
        else:
            x_center = wdgt.winfo_rootx() + wdgt.winfo_width() + 10
            y_center = wdgt.winfo_rooty()
        pop.geometry(f"+{x_center}+{y_center}")

    def tooltip(self, wdgt, txt, view=True, font=10):
        wdgt.bind('<Enter>', lambda x: self.pop_tooltip(wdgt, txt, view, font))

    def destroy_reference_data(self):
        if len(self.reference_data) != 0:
            for i in self.reference_data:
                i.destroy()
            self.reference_data = []

    def create_nice_button(self, text, command, photo, height, width, font=24):
        dec = CTkButton(self.root,
                        text=text,
                        command=command,
                        image=photo,
                        height=height,
                        width=width,
                        font=('Bookman Old Style', font),
                        fg_color='#a78950',
                        hover_color='#7e612b',
                        corner_radius=0
                        )
        return dec

    def create_nice_label(self, text, height, width, font=24):
        dec = CTkLabel(self.root,
                       text=text,
                       text_color='white',
                       height=height,
                       width=width,
                       font=('Bookman Old Style', font),
                       fg_color='#c7a463',
                       corner_radius=0)
        return dec

    def economic_button(self):
        photo = PhotoImage(file='../resources/images/иконка экономики 15-06.png')
        press = self.create_nice_button('', self.show_economics_decisions, photo, 80, 80)
        self.tooltip(press, 'Экономические решения')
        return press

    def show_economics_decisions(self):
        self.destroy_reference_data()
        self.reference_data.append(self.create_nice_label('Экономические решения', 40, 320))
        for i in range(5):
            self.reference_data.append(self.create_nice_button('Экономическое решение ' + str(i), None, None, 40, 300, 18))
        self.canvas.create_window(1490, 120, anchor="nw", window=self.reference_data[0])
        for i in range(1, len(self.reference_data)):
            self.canvas.create_window(1500, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def politic_button(self):
        photo = PhotoImage(file='../resources/images/иконка политики 15-06.png')
        press = self.create_nice_button('', self.show_politic_decisions, photo, 80, 80)
        self.tooltip(press, 'Политические решения')
        return press

    def show_politic_decisions(self):
        self.destroy_reference_data()
        self.reference_data.append(self.create_nice_label('Политическое решения', 40, 320))
        FAC1 = Decision("../resources/decisions/FAC1.json", self.player)
        FAC1_button = self.create_nice_button(FAC1.name_ru, FAC1.apply, None, 40, 300, 18)
        self.tooltip(FAC1_button, FAC1.tooltip, False, 14)
        self.reference_data.append(FAC1_button)
        self.canvas.create_window(1490, 120, anchor="nw", window=self.reference_data[0])
        for i in range(1, len(self.reference_data)):
            self.canvas.create_window(1400, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def government_button(self):
        photo = PhotoImage(file='../resources/images/иконка государства 16-06.png')
        press = self.create_nice_button('', self.show_government_information, photo, 80, 80)
        self.show_government_information()
        self.tooltip(press, "Информация о государстве")
        return press

    def show_government_information(self):
        self.destroy_reference_data()
        economics = self.player.economics
        self.update_proportions()
        self.reference_data.append(self.create_nice_label('Информация о государстве', 40, 420))
        self.reference_data.append(self.create_nice_label('Имя : ' + self.player.name, 40, 310))
        self.reference_data.append(self.create_nice_label('⚖Стабильность ' + str(self.player.stability) + '%', 40, 310))
        for i in range(len(economics.sectors_name_ru)):
            sector = economics.sectors[economics.sectors_name[i]]
            self.reference_data.append(self.create_nice_label(economics.sectors_codes[i] +
                                                              economics.sectors_name_ru[i], 40, 250))
            value = self.create_nice_button(sector.value, None, None, 40, 50, 18)
            proportion = self.create_nice_button(str(sector.proportion) + '%', None, None, 40, 50, 18)
            tooltip_text = str(sector.k_buff) + ' ⌃\n' + \
                           str(sector.k_debuff) + ' ⌄'
            self.tooltip(value, tooltip_text, False)
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


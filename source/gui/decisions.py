from customtkinter import *
from tkinter import *


class DecisionsGUI:
    def __init__(self, root, canvas, player):
        self.reference_data = []
        self.root = root
        self.canvas = canvas
        self.player = player

    def pop_tooltip(self, wdgt, txt, view=True):
        pop = Toplevel(wdgt)
        pop.overrideredirect(True)
        Label(pop, text=txt, font=('Bookman Old Style', 10), bg='#ECE2AE', borderwidth=2).pack()
        wdgt.bind('<Leave>', lambda x: pop.destroy())
        if view:
            x_center = wdgt.winfo_rootx() - 20
            y_center = wdgt.winfo_rooty() + wdgt.winfo_height() + 5
        else:
            x_center = wdgt.winfo_rootx() + wdgt.winfo_width() + 10
            y_center = wdgt.winfo_rooty()
        pop.geometry(f"+{x_center}+{y_center}")

    def tooltip(self, wdgt, txt, view=True):
        wdgt.bind('<Enter>', lambda x: self.pop_tooltip(wdgt, txt, view))

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
        for i in range(7):
            self.reference_data.append(self.create_nice_button('Политическое решение ' + str(i), None, None, 40, 300, 18))
        self.canvas.create_window(1490, 120, anchor="nw", window=self.reference_data[0])
        for i in range(1, len(self.reference_data)):
            self.canvas.create_window(1500, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def government_button(self):
        photo = PhotoImage(file='../resources/images/иконка государства 16-06.png')
        press = self.create_nice_button('', self.show_government_information, photo, 80, 80)
        self.show_government_information()
        self.tooltip(press, "Информация о государстве")
        return press

    def show_government_information(self):
        self.destroy_reference_data()
        economics = self.player.economics
        self.reference_data.append(self.create_nice_label('Информация о государстве', 40, 420))
        self.reference_data.append(self.create_nice_label('Имя : ' + self.player.name, 40, 310))
        for i in range(len(economics.sectors_name_ru)):
            self.reference_data.append(self.create_nice_label(economics.sectors_name_ru[i], 40, 250))
            value = self.create_nice_button(economics.sectors[economics.sectors_name[i]].value, None, None, 40, 50, 18)
            tooltip_text = str(economics.sectors[economics.sectors_name[i]].k_buff) + ' boost \n' + \
                           str(economics.sectors[economics.sectors_name[i]].k_debuff) + ' retard'
            self.tooltip(value, tooltip_text, False)
            self.reference_data.append(value)
        self.canvas.create_window(1450, 120, anchor="nw", window=self.reference_data[0])
        self.canvas.create_window(1500, 170, anchor="nw", window=self.reference_data[1])
        for i in range(2, len(self.reference_data), 2):
            self.canvas.create_window(1500, 170 + i * 25, anchor="nw", window=self.reference_data[i])
            self.canvas.create_window(1760, 170 + i * 25, anchor="nw", window=self.reference_data[i + 1])


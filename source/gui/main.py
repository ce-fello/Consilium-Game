from customtkinter import *
from tkinter import *
from tktooltip import ToolTip  # pip install tkinter-tooltip
from source.server.Player import Player
from source.server.Economics import Economics


class GameUI:
    def __init__(self, player: Player):
        self.player = player
        self.root = CTk()

        self.root.title('Consilium')
        self.root.geometry('600x350')
        self.root.attributes('-fullscreen', True)

        image_path = "../resources/images/Фон 15-06-1.png"
        bg_image = PhotoImage(file=image_path)

        self.reference_data = []

        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=bg_image)

        self.canvas.create_window(self.root.winfo_screenwidth() * 0.8, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.economic_button())
        self.canvas.create_window(self.root.winfo_screenwidth() * 0.85, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.politic_button())
        self.canvas.create_window(self.root.winfo_screenwidth() * 0.75, self.root.winfo_screenheight() * 0.01,
                                  anchor="nw", window=self.government_button())

        self.root.mainloop()

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
        ToolTip(press, msg="Экономические решения", delay=0.01, follow=True)
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
        ToolTip(press, msg="Политические решения", delay=0.01, follow=True)
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
        ToolTip(press, msg="Информация о государстве", delay=0.01, follow=True)
        return press

    def show_government_information(self):
        self.destroy_reference_data()
        economics = self.player.economics
        self.reference_data.append(self.create_nice_label('Информация о государстве', 40, 420))
        self.reference_data.append(self.create_nice_label('Имя : ' + self.player.name, 40, 310))
        for i in range(len(economics.sectors_name_ru)):
            self.reference_data.append(self.create_nice_label(economics.sectors_name_ru[i], 40, 250))
            self.reference_data.append(self.create_nice_label(economics.sectors[economics.sectors_name[i]].value, 40, 50))
        self.canvas.create_window(1450, 120, anchor="nw", window=self.reference_data[0])
        self.canvas.create_window(1500, 170, anchor="nw", window=self.reference_data[1])
        for i in range(2, len(self.reference_data), 2):
            self.canvas.create_window(1500, 170 + i * 25, anchor="nw", window=self.reference_data[i])
            self.canvas.create_window(1760, 170 + i * 25, anchor="nw", window=self.reference_data[i + 1])


sectors_value = [100, 30, 10, 10, 25, 30]
sectors_k_buff = [1, 1, 1, 1, 1, 0.8]
sectors_k_debuff = [0.9, 0.9, 0.9, 1.1, 1.1, 0.9]
example_player = Player(0, '83 ПО ИНФЕ', Economics(sectors_value, sectors_k_buff, sectors_k_debuff))
game = GameUI(example_player)



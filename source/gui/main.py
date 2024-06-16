from customtkinter import *
from tkinter import *
from idlelib.tooltip import Hovertip
from tktooltip import ToolTip  # pip install tkinter-tooltip


class GameUI:
    def __init__(self):
        self.root = CTk()

        self.root.title('Conlisium')
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

    def economic_button(self):
        photo = PhotoImage(file='../resources/images/иконка экономики 15-06.png')
        press = CTkButton(self.root,
                          text='',
                          command=self.press_economics_decisions,
                          image=photo,
                          height=80,
                          width=80,
                          font=('Bookman Old Style', 24),
                          fg_color='#a78950',
                          hover_color='#7e612b',
                          corner_radius=0
                          )
        ToolTip(press, msg="Экономические решения", delay=0.01, follow=True)
        return press

    def press_economics_decisions(self):
        if len(self.reference_data) != 0:
            for i in self.reference_data:
                i.destroy()
            self.reference_data = []
        for i in range(5):
            dec = CTkButton(self.root,
                            text='Экономическое решение ' + str(i),
                            command=None,
                            height=40,
                            width=300,
                            font=('Bookman Old Style', 18),
                            fg_color='#a78950',
                            hover_color='#7e612b',
                            corner_radius=0
                            )
            self.reference_data.append(dec)
        for i in range(len(self.reference_data)):
            self.canvas.create_window(1500, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def politic_button(self):
        photo = PhotoImage(file='../resources/images/иконка политики 15-06.png')
        press = CTkButton(self.root,
                          text='',
                          command=self.press_politic_decisions,
                          image=photo,
                          height=80,
                          width=80,
                          font=('Bookman Old Style', 24),
                          fg_color='#a78950',
                          hover_color='#7e612b',
                          corner_radius=0
                          )
        ToolTip(press, msg="Политические решения", delay=0.01, follow=True)
        return press

    def press_politic_decisions(self):
        if len(self.reference_data) != 0:
            for i in self.reference_data:
                i.destroy()
            self.reference_data = []
        for i in range(7):
            dec = CTkButton(self.root,
                            text='Политическое решение ' + str(i),
                            command=None,
                            height=40,
                            width=300,
                            font=('Bookman Old Style', 18),
                            fg_color='#a78950',
                            hover_color='#7e612b',
                            corner_radius=0
                            )
            self.reference_data.append(dec)
        for i in range(len(self.reference_data)):
            self.canvas.create_window(1500, 120 + i * 50, anchor="nw", window=self.reference_data[i])

    def government_button(self):
        photo = PhotoImage(file='../resources/images/иконка государства 16-06.png')
        press = CTkButton(self.root,
                          text='',
                          command=None,
                          image=photo,
                          height=80,
                          width=80,
                          font=('Bookman Old Style', 24),
                          fg_color='#a78950',
                          hover_color='#7e612b',
                          corner_radius=0
                          )
        ToolTip(press, msg="Информация о государстве", delay=0.01, follow=True)
        return press


game = GameUI()



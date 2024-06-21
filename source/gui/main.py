from customtkinter import *
from tkinter import *
from idlelib.tooltip import Hovertip
from tktooltip import ToolTip  # pip install tkinter-tooltip
from source.server.Player import Player
from source.server.Economics import Economics
from decisions_gui import DecisionsGUI
from stats_gui import StatsGUI


class GameUI:
    def __init__(self, player: Player):
        self.player = player
        self.root = CTk()

        self.root.title('Conlisium')
        self.root.geometry('600x350')
        self.root.attributes('-fullscreen', True)

        image_path = "../resources/images/background.png"
        bg_image = PhotoImage(file=image_path)

        self.reference_data = []

        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=bg_image)

        DecisionsGUI(self.root, self.canvas, self.player)
        StatsGUI(self.root, self.canvas, self.player)

        self.root.mainloop()


sectors_value = [100, 30, 10, 10, 25, 30]
sectors_k_buff = [1, 1, 1, 1, 1, 0.8]
sectors_k_debuff = [0.9, 0.9, 0.9, 1.1, 1.1, 0.9]
example_player = Player(0, 'Боливия', 17, Economics(sectors_value, sectors_k_buff, sectors_k_debuff))
game = GameUI(example_player)



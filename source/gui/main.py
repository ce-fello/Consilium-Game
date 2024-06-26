from customtkinter import *
from tkinter import *
from source.server.Player import Player
from source.server.Economics import Economics
from source.server.Time import Time
from source.server.Map import Map
from source.server.Cell import Cell
from source.server.Game import Game
from source.gui.time_gui import TimeGUI
from decisions_gui import DecisionsGUI
from stats_gui import StatsGUI


class GameUI:
    def __init__(self, game: Game, player: Player):
        self.player = player
        self.root = CTk()
        self.game = game

        self.root.title('Consilium')
        self.root.geometry('600x350')
        self.root.attributes('-fullscreen', True)

        image_path = "../resources/images/background.png"
        bg_image = PhotoImage(file=image_path)

        self.reference_data = []

        self.canvas = Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=bg_image)

        self.decisions = DecisionsGUI(self.root, self.canvas, self.game, self.player)
        self.stats = StatsGUI(self.root, self.canvas, self.player)
        self.time_counter = TimeGUI(self.root, self.canvas, self.game, self.player)

        self.stats.show()

        self.root.after(100, self.update_screen())

        self.root.mainloop()

    def update_screen(self):
        self.time_counter.update_date()
        self.game.time.mode = self.time_counter.Timer_mode.get()
        self.stats.update_stats()
        self.decisions.update_reference_data()
        self.root.update()
        self.root.after(100, self.update_screen)


sectors_value = [100, 30, 10, 10, 25, 30]
sectors_k_buff = [1, 1, 1, 1, 1, 0.8]
sectors_k_debuff = [0.9, 0.9, 0.9, 1.1, 1.1, 0.9]
example_player = Player(0, 'Боливия', 50, Economics(sectors_value, sectors_k_buff, sectors_k_debuff))
timer = Time()
map = Map([Cell(1, '', [1], '')])
game = Game([example_player], map, timer)
GameUI(game, example_player)

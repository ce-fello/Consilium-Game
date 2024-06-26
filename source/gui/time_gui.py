from customtkinter import *
import datetime
from source.server.Decision import Decision
from tkinter import *
from os import listdir
from os.path import isfile, join
from standard_gui import StandardFunctions
from source.server.Game import Game
from source.server.Player import Player
from source.gui.stats_gui import StatsGUI


class TimeGUI:
    def __init__(self, root, canvas, game: Game, player: Player):
        self.root = root
        self.canvas = canvas
        self.game = game
        self.standard = StandardFunctions(self.root)
        self.player = player
        self.modes_names = ["день/2 сек", "день/сек", "2 дня/сек"]
        self.modes_widgets = []
        self.Timer_mode = IntVar(value=0)
        self.date_label = self.standard.create_nice_label(self.game.time.data, 50, 210, 24)
        self.show_date()

    def selection(self):
        self.game.time.mode = self.Timer_mode

    def show_date(self):
        for i in range(len(self.modes_names)):
            mode1 = CTkRadioButton(self.root, text=self.modes_names[i], variable=self.Timer_mode, value=i,
                                   width=112, height=10,
                                   command=self.selection, fg_color='white', hover_color='#7e612b',
                                   bg_color='#c7a463', border_color='#464646', border_width_unchecked=3,
                                   border_width_checked=6, font=('Bookman Old Style', 14), text_color='white')
            self.modes_widgets.append(mode1)

        for i in range(len(self.modes_widgets)):
            self.canvas.create_window(800 + 122 * i, 80, anchor="nw", window=self.modes_widgets[i])

        pause_photo = PhotoImage(file='../resources/images/pause_icon.png')
        play_photo = PhotoImage(file='../resources/images/play_icon.png')

        pause_button = self.standard.create_nice_button('', self.pause, pause_photo, 50, 50)
        play_button = self.standard.create_nice_button('', self.start, play_photo, 50, 50)

        self.standard.tooltip(pause_button, 'остановить время')
        self.standard.tooltip(play_button, 'запустить время')

        self.canvas.create_window(800, 10, anchor="nw", window=pause_button)
        self.canvas.create_window(1100, 10, anchor="nw", window=play_button)

        self.date_label = self.standard.create_nice_label(self.game.time.data, 50, 210, 24)

        self.date_label.configure(font=("Bookman Old Style", 24, "bold"))
        self.date_label.configure(text_color='#464646')

        self.canvas.create_window(870, 10, anchor="nw", window=self.date_label)

    def pause(self):
        self.game.time.start = False
        self.date_label.configure(text_color='#464646')

    def start(self):
        self.game.time.start = True
        self.date_label.configure(text_color='white')
        self.game.time.current_moment = datetime.datetime.now()

    def update_date(self):
        self.game.time.working()
        self.date_label.configure(text=self.game.time.data)


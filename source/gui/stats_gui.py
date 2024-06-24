from standard_gui import StandardFunctions
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
import numpy as np


class StatsGUI:
    def __init__(self, root, canvas, player):
        self.root = root
        self.canvas = canvas
        self.player = player
        self.standard = StandardFunctions(self.root)
        self.show_stability()
        self.show_budget()

    def show_stability(self):
        stability_photo = PhotoImage(file='../resources/images/scales_icon.png')

        first_photo = PhotoImage(file=f'../resources/images/numbers/{str(self.player.stability)[0]}.png')
        second_photo = PhotoImage(file=f'../resources/images/numbers/{str(self.player.stability)[1]}.png')
        third_photo = PhotoImage(file=f'../resources/images/numbers/%.png')

        self.canvas.create_window(500, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, stability_photo, 80, 80))
        self.canvas.create_window(580, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, first_photo, 80, 40))
        self.canvas.create_window(620, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, second_photo, 80, 40))
        self.canvas.create_window(660, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, third_photo, 80, 40))

    def show_budget(self):
        stability_photo = PhotoImage(file='../resources/images/budget_icon.png')
        budget = 0
        for i in self.player.economics.sectors_name:
            budget += self.player.economics.sectors[i].value
        budget_photos = []
        for i in str(budget):
            if i != '.':
                budget_photos.append(PhotoImage(file=f'../resources/images/numbers/{i}.png'))
            else:
                budget_photos.append(PhotoImage(file=f'../resources/images/numbers/dot.png'))

        self.canvas.create_window(1000, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, stability_photo, 80,
                                                                                   80))
        for i in range(len(budget_photos)):
            self.canvas.create_window(1080 + 40 * i, 10, anchor="nw",
                                      window=self.standard.create_nice_no_hover_button("", None, budget_photos[i], 80, 40))








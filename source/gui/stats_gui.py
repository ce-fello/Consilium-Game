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

    def show_stability(self):
        stability_photo = PhotoImage(file='../resources/images/scales_icon.png')

        first_photo = PhotoImage(file=f'../resources/images/numbers/{str(self.player.stability)[0]}.png')
        second_photo = PhotoImage(file=f'../resources/images/numbers/{str(self.player.stability)[1]}.png')
        third_photo = PhotoImage(file=f'../resources/images/numbers/%.png')

        self.canvas.create_window(100, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, stability_photo, 80, 80))
        self.canvas.create_window(180, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, first_photo, 80, 40))
        self.canvas.create_window(220, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, second_photo, 80, 40))
        self.canvas.create_window(263, 10, anchor="nw",
                                  window=self.standard.create_nice_no_hover_button("", None, third_photo, 80, 40))








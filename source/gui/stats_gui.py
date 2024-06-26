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
        self.stability_button = self.make_stability_button()
        self.budget_button = self.make_budget_button()

    def show(self):
        self.show_stability()
        self.show_budget()
        self.show_close()

    def show_stability(self):
        self.stability_button.destroy()
        self.stability_button = self.make_stability_button()
        self.canvas.create_window(570, 10, anchor="nw", window=self.stability_button)

    def make_stability_button(self):
        stability_photo = PhotoImage(file='../resources/images/scales_icon.png')

        stability_button = self.standard.create_nice_button(str(self.player.stability) + '%', None,
                                                                 stability_photo, 80, 180)

        self.standard.tooltip(stability_button, 'стабильность')

        return stability_button

    def show_budget(self):
        self.budget_button.destroy()
        self.budget_button = self.make_budget_button()
        self.canvas.create_window(1200, 10, anchor="nw", window=self.budget_button)

    def make_budget_button(self):
        budget_photo = PhotoImage(file='../resources/images/budget_icon.png')

        budget = 0
        for i in self.player.economics.sectors_name:
            budget += self.player.economics.sectors[i].value

        budget_button = self.standard.create_nice_button(str(budget) + '💰', None, budget_photo, 80, 180)

        self.standard.tooltip(budget_button, 'валовой внутренний продукт')

        return budget_button

    def show_close(self):
        close_photo = PhotoImage(file='../resources/images/close_icon.png')

        close_button = self.standard.create_nice_button('',
                                                        self.root.destroy, close_photo, 60, 60)

        self.standard.tooltip(close_button, 'закрыть игру')

        self.canvas.create_window(1820, 20, anchor="nw", window=close_button)









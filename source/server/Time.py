import datetime
from tkinter import *
from customtkinter import *


class Time:
    def __init__(self):
        self.data = datetime.date(1900, 1, 2)
        self.mode = 0
        self.start = False
        self.update_sectors = False
        self.update_decisions = False
        self.current_moment = datetime.datetime.now()

    def working(self):
        if self.start:
            if self.mode == 0:
                if (datetime.datetime.now() - self.current_moment).total_seconds() > 2:
                    self.current_moment = datetime.datetime.now()
                    self.data += datetime.timedelta(days=1)
                    if self.data.day == 1:
                        self.update_sectors = True
                        self.update_decisions = True
            elif self.mode == 1:
                if (datetime.datetime.now() - self.current_moment).total_seconds() > 1:
                    self.current_moment = datetime.datetime.now()
                    self.data += datetime.timedelta(days=1)
                    if self.data.day == 1:
                        self.update_sectors = True
                        self.update_decisions = True
            elif self.mode == 2:
                if (datetime.datetime.now() - self.current_moment).total_seconds() > 0.5:
                    self.current_moment = datetime.datetime.now()
                    self.data += datetime.timedelta(days=1)
                    if self.data.day == 1:
                        self.update_sectors = True
                        self.update_decisions = True

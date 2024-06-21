from customtkinter import *
from tkinter import *


class StandardFunctions:
    def __init__(self, root):
        self.root = root

    def pop_tooltip(self, wdgt, txt, view=True, font=10):
        pop = Toplevel(wdgt)
        pop.overrideredirect(True)
        Label(pop, text=txt, font=('Bookman Old Style', font), bg='#ECE2AE', borderwidth=2).pack()
        wdgt.bind('<Leave>', lambda x: pop.destroy())
        if view:  # lower
            x_center = wdgt.winfo_rootx() - 20
            y_center = wdgt.winfo_rooty() + wdgt.winfo_height() + 5
        else:  # right
            x_center = wdgt.winfo_rootx() + wdgt.winfo_width() + 10
            y_center = wdgt.winfo_rooty()
        pop.geometry(f"+{x_center}+{y_center}")

    def tooltip(self, wdgt, txt, view=True, font=10):
        wdgt.bind('<Enter>', lambda x: self.pop_tooltip(wdgt, txt, view, font))

    def create_nice_button(self, text, command, photo, height, width, font=24, text_color='white'):
        dec = CTkButton(self.root,
                        text=text,
                        command=command,
                        image=photo,
                        text_color=text_color,
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

    def create_nice_no_hover_button(self, text, command, photo, height, width, font=24, text_color='white'):
        dec = CTkButton(self.root,
                        text=text,
                        command=command,
                        image=photo,
                        text_color=text_color,
                        height=height,
                        width=width,
                        font=('Bookman Old Style', font),
                        fg_color='#a78950',
                        hover_color='#a78950',
                        corner_radius=0
                        )
        return dec


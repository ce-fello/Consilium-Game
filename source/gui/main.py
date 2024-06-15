from customtkinter import *
from tkinter import PhotoImage
from tkinter import *

root = CTk()

root.title('Conlisium')
root.geometry('600x350')
root.attributes('-fullscreen', True)


def hello():
    canvas.create_text(500, 120, text="Привет, мир!", font=("Bookman Old Style", 20), fill="black")


image_path = "Фон 15-06-1.png"
bg_image = PhotoImage(file=image_path)

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_image)

my_button = CTkButton(root,
                      text='Кнопка',
                      command=hello,
                      height=40,
                      width=100,
                      font=('Bookman Old Style', 24),
                      fg_color='#a78950',
                      hover_color='#7e612b',
                      corner_radius=0
                      )

canvas.create_window(500, 20, anchor="nw", window=my_button)

root.mainloop()

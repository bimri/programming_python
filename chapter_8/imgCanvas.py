# Canvas widgets: can display pictures too.

gifdir = r"C:\Users\avatar\Pictures\gifs"
from tkinter import *

win = Tk()
img = PhotoImage(file=gifdir + "/09721270674669.5beaf52a3427d.png")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)                # x, y coordiantes

win.mainloop()

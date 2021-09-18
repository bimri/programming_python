gifdir = r"C:\Users\avatar\Pictures\gifs"
from tkinter import *
from sys import argv
filename = argv[1] if len(argv) > 1 else "/09721270674669.5beaf52a3427d.png"        # name on cmdline

win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())          # size to img size
can.create_image(2, 2, image=img, anchor=NW)                # x, y coordiantes
win.mainloop()

"Images"
'''
In tkinter, graphical images are displayed by creating independent PhotoImage or
BitmapImage objects, and then attaching those image objects to other widgets via
image attribute settings. Buttons, labels, canvases, text, and menus can display images
by associating prebuilt image objects in this way.
'''

gifdir = r"C:\Users\avatar\Pictures\gifs"
from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir + "/a0658a70674669.5bc749c1cb1b7.png")
Button(win, image=img).pack()
win.mainloop()


'''
PhotoImage and its cousin, BitmapImage, essentially load graphics files and allow those
graphics to be attached to other kinds of widgets. To open a picture file, pass its name
to the file attribute of these image objects.
'''

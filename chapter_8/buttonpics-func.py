"Fun with Buttons and Pictures"

from tkinter import *                                           # get base widget set
from glob import glob                                           # filename expansion list
import demoCheck                                                # attach checkbutton demo to me
import random                                                   # pick a picture at random
gifdir = r"C:\Users\avatar\Pictures\gifs"                       # where to look for GIF files


def draw():
    name, photo = random.choice(image_names)
    lbl.config(text=name)
    pix.config(image=photo)


root = Tk()
lbl  = Label(root, text="none", bg='blue', fg='red')
pix  = Button(root, text='Press me', command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)


files = glob(gifdir + ".png")                                   # PNGs for now
images = [(x, PhotoImage(file=x)) for x in files]               # load and hold
print(files)
root.mainloop()


"""
This code uses a handful of built-in tools from the Python library:
    • The Python glob module gives a list of all files ending
    in .gif in a directory; in other words, all GIF files stored there.
    
    • The Python random module is used to select a random GIF from files in the directory:
    random.choice picks and returns an item from a list at random.
    
    • To change the image displayed (and the GIF file’s name in a label at the top of the
    window), the script simply calls the widget config method with new option settings;
    changing on the fly like this changes the widget’s display dynamically.
"""


'''
Notice how this script builds and holds on to all images in its images list. The list
comprehension here applies a PhotoImage constructor call to every .gif file in the photo
directory, producing a list of (filename, imageobject) tuples that is saved in a global
variable (a map call using a one-argument lambda function could do the same). Remember,
this guarantees that image objects won’t be garbage collected as long as the program
is running.
'''
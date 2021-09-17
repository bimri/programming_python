"Letting users select colors on the fly"
'''
The standard color selection dialog isn’t just another pretty face—scripts can pass the
hexadecimal color string it returns to the bg and fg widget color configuration options

This adds another dimension of customization to tkinter GUIs: instead of hardcoding
colors in your GUI products, you can provide a button that pops up color selectors that
let users choose color preferences on the fly. Simply pass the color string to widget
config methods in callback handlers.
'''

from tkinter import * 
from tkinter.colorchooser import askcolor

def setBgColor():
    (triple, hexstr) = askcolor()
    if hexstr:
        print(hexstr)
        push.config(bg=hexstr)

root = Tk()
push = Button(root, text='Set Backgroung Color', command=setBgColor)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop()
 
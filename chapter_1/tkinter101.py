"Step 5: Adding a GUI"
'GUI Basics'
# implements a GUI with a button that runs the reply function each time it is pressed.


from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='popup', message='Button pressed!')


window = Tk()   
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()

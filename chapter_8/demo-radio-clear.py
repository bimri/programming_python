"Hold onto your variables!"
'''
One minor word of caution: you should generally hold onto the tkinter variable object
used to link radio buttons for as long as the radio buttons are displayed.
'''

# hold on to your radio variables (an obscure thing, indeed)

from tkinter import *
root = Tk()


def radio1():
    #global tmp                         # local vars are temporary
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)                          # select 6th button

radio1()
root.mainloop()


'''
Uncommenting
the global statement here makes 5 start out set, as expected.
'''

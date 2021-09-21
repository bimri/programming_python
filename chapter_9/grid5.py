# 2D table of input fields, default Tk root window

from tkinter import *

rows = []
for i in range(5):
    cols = []
    for j in range(4):
        ent = Entry(relief=RIDGE)
        ent.grid(row=i, column=j, sticky=NSEW)
        ent.insert(END, '%d.%d' % (i, j))
        cols.append(ent)
    rows.append(cols)

def onPress():
    for row in rows:
        for col in row:
            print(col.get(), end=' ')
        print()
    

Button(text='Fetch', command=onPress).grid()
mainloop()


'''
When run, this script creates the window and saves away all the grid’s
entry field widgets in a two-dimensional list of lists. When its Fetch button is pressed,
the script steps through the saved list of lists of entry widgets, to fetch and display all
the current values in the grid. Here is the output of two Fetch presses—one before I
made input field changes, and one after:
'''

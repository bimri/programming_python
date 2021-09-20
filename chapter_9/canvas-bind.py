"Binding events on specific items"
'''
Much like we did for the Text widget, it is also possible to bind events for one or more
specific objects drawn on a Canvas with its tag_bind method. This call accepts either a
tag name string or an object ID in its first argument.
'''
# bind events on both canvas and its items
from tkinter import *

def onCanvasClick(event):
    print('Got canvas Click', event.x, event.y, event.widget)

def onObjectClick(event):
    print('Got object click', event.x, event.y, event.widget, end=' ')
    print(event.widget.find_closest(event.x, event.y))                      # find text object's ID

root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50, 30, text='Click me one')
obj2 = canv.create_text(50, 70, text='Click me two')

canv.bind('<Double-1>', onCanvasClick)                                      # bind to whole canvas
canv.tag_bind(obj1, '<Double-1>', onObjectClick)                            # bind to drawn item
canv.tag_bind(obj2, '<Double-1>', onObjectClick)                            # a tag works here too
canv.pack()
root.mainloop()

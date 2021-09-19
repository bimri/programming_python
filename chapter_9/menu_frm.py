"Frame- and Menubutton-Based Menus"
'''
Although these are less commonly used for top-level windows, it’s also possible to
create a menu bar as a horizontal Frame. Before I show you how, though, let me explain
why you should care. Because this frame-based scheme doesn’t depend on top-level
window protocols, it can also be used to add menus as nested components of larger
displays. In other words, it’s not just for top-level windows.

To make one, simply pack Menubutton widgets within a
Frame container, associate Menu widgets with the Menubuttons, and associate the Frame
with the top of a container window.
'''

# Frame-based menus: for top-levels and components

from tkinter import *                               # get widget classes
from tkinter.messagebox import *                    # get standard dialogs
 
def notdone():
    showerror('Not implemented', 'Not yet available')

def makemenu(parent):
    menubar = Frame(parent)                                                 # relief=RAISED, bd=2...: make a Frame for the menubar
    menubar.pack(side=TOP, fill=X)

    fbutton = Menubutton(menubar, text='File', underline=0)                 # attach a Menubutton to Frame     
    fbutton.pack(side=LEFT)
    file = Menu(fbutton)                                                    # attach a Menu to Menubutton
    file.add_command(label='New...', command=notdone, underline=0)
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit', command=parent.quit, underline=0)
    fbutton.config(menu=file)                                               # crosslink button to menu

    ebutton = Menubutton(menubar, text='Edit', underline=0)
    ebutton.pack(side=LEFT)
    edit = Menu(ebutton, tearoff=False)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    ebutton.config(menu=edit)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=parent.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)
    return menubar


if __name__ == '__main__':
    root = Tk()                                             # or TopLevel or Frame
    root.title('menu_frm')                                  # set window-mgr info
    makemenu(root)                                          # associate a menu bar
    msg = Label(root, text='Frame menu basics')             # add something below
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop() 


'''
The biggest advantage of frame-based menu bars, though, is that they can also be attached
as nested components in larger displays.
'''

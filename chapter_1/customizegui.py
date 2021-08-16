"Step 5: Adding a GUI"
'Using OOP for GUIs'
'''
Moreover, because MyGui is coded as a class, the GUI can be customized by the usual
inheritance mechanism; simply define a subclass that replaces the parts that differ. The
reply method, for example, can be customized this way to do something unique
'''


from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui


class CustomGui(MyGui):                                             # inherit init
    def reply(self):                                                # redefine reply
        showinfo(title='popup', message='Ouch!')                    # replace button
    


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()

"tkinter Coding Alternatives"
'''
there are a variety of ways to code the gui1 example. For instance,
if you want to make all your tkinter imports more explicit in your script, grab the whole
module and prefix all of its names with the module’s name
'''
# import versus from
import tkinter
widget = tkinter.Label(None, text='Hello GUI World!')
widget.pack()
widget.mainloop()


'''
The tkinter module goes out of its way to export only what we really need, so it’s one
of the few for which the * import form is relatively safe to apply.‖
'''

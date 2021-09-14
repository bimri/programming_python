"Configuring Widget Options and Window Titles"
# options keys

from tkinter import *
widget = Label()
widget['text'] = 'Hello GUI World'
# widget['bg'] = 'red'
# widget['fg'] = 'white'
# widget['font'] = ('times', 20, 'italic')
# widget['width'] = 10
# widget['height'] = 5
# widget['relief'] = 'sunken'
# widget['borderwidth'] = 10
# widget['anchor'] = 'center'
# widget['justify'] = 'left'
# widget['textvariable'] = StringVar()
# widget['textvariable'].set('Hello World')
# widget['compound'] = 'left'
# widget['image'] = PhotoImage(file='../gifs/PythonPowered.gif')
# widget['state'] = 'disabled'
# widget['underline'] = 5
# widget['wraplength'] = 200
# widget['cursor'] = 'pirate'
# widget['command'] = lambda: None
widget.pack(side='top')
widget.mainloop()

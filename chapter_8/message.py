"Message and Entry"
'''
The Message and Entry widgets allow for display and input of simple text. Both are
essentially functional subsets of the Text widget; Text can do everything
Message and Entry can, but not vice versa.
'''

"Message"
'''
The Message widget is simply a place to display text.
Message splits up long strings automatically and flexibly 
and can be embedded inside container widgets
any time you need to add some read-only text to a display.
'''

from tkinter import *
msg = Message(text="Oh by the way, which one's Pink?")
msg.config(bg='pink', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)
mainloop()

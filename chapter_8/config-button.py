from tkinter import *

widget = Button(text='bimri', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='purple', fg='white')
widget.config(font=('helvetica', 15, 'underline italic'))
mainloop()

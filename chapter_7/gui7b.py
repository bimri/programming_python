 from tkinter import *
from gui7 import HelloPackage                       # or get from gui7c--__getattr__ added

frm = Frame()
frm.pack()
Label(frm, text='Hello, world').pack()

part = HelloPackage(frm)
part.pack(side=RIGHT)                               # FAILS!--need part.top.pack(side=RIGHT)
frm.mainloop()

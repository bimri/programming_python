# check buttons, the easy way

from tkinter import * 
root = Tk()
states = []
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=LEFT)
    states.append(var)
root.mainloop()                             # let tkinter keep track
print([var.get() for var in states])        # show all states on exit (or map/lambda)


"""
The point here is that you don’t necessarily have to link variables with check buttons,
but your GUI life will be simpler if you do. The list comprehension at the very end of
this script, by the way, is equivalent to the following unbound method and lambda/
bound-method map call forms:
    print(list(map(IntVar.get, states)))
    print(list(map(lambda var: var.get(), states)))
"""

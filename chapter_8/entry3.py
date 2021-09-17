"tkinter “Variables” and Form Layout Alternatives"
'''
Entry widgets (among others) support the notion of an associated variable—changing
the associated variable changes the text displayed in the Entry, and changing the text
in the Entry changes the value of the variable. These aren’t normal Python variable
names, though. Variables tied to widgets are instances of variable classes in the tkinter
module library. These classes are named StringVar, IntVar, DoubleVar, and Boolean
Var; you pick one based on the context in which it is to be used.
'''

"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""

from tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())             # get from var

def makeform(root, fields):
    form = Frame(root)                                      # make outer frame
    left = Frame(form)                                      # make two columns
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)               # grow horizontal

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)              # add to columns
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)                        # link field to var
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()


'''
the window is laid
out differently—as a Frame containing two nested subframes used to build the left and
right columns of the form area

The main thing to notice here, though, is the use of StringVar variables. Instead of using
a list of Entry widgets to fetch input values, this version keeps a list of StringVar objects
that have been associated with the Entry widgets, like this:
    ent = Entry(rite)
    var = StringVar()
    ent.config(textvariable=var)                # link field to var

Once you’ve tied variables in this way, changing and fetching the variable’s value:
    var.set('text here')
    value = var.get()
will really change and fetch the corresponding display’s input field value.* The variable
object get method returns as a string for StringVar, an integer for IntVar, and a floatingpoint
number for DoubleVar.  

So, why the bother about variable objects?
For one thing, it clears up that nasty fetch-after-destroy peril we met in the prior section.
Because StringVars live on after the Entry widgets they are tied to have been destroyed,
it’s OK to fetch input values from them long after a modal dialog has been dismissed.
'''

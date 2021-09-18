"Check buttons and variables"
'''
Linked variables may seem superfluous at first glance, 
but they simplify some GUI chores.

Keep in mind that a Checkbutton’s command callback will be run on every press, whether
the press toggles the check button to a selected or a deselected state. Because of that,
if you want to run an action immediately when a check button is pressed, you will
generally want to check the button’s current value in the callback handler. Because
there is no check button “get” method for fetching values, you usually need to interrogate
an associated variable to see if the button is on or off.

Moreover, some GUIs simply let users set check buttons without running command callbacks
at all and fetch button settings at some later point in the program.
'''

# check buttons, the hard way (without variables)

from tkinter import * 
states = []                             # change object not name
def onPress(i):                         # keep track of states
    states[i] = not states[i]           # changes False->True, True->False

root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)
root.mainloop()
print(states)                           # show all states on exit


'''
The lambda here passes along the pressed button’s index in the states list. Otherwise,
we would need a separate callback function for each button. Here again, we need to
use a default argument to pass the loop variable into the lambda, or the loop variable
will be its value on the last loop iteration for all 10 of the generated functions
'''

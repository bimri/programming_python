"Step 5: Adding a GUI"
'A GUI Shelve Interface'
'''
For our database application, the first thing we probably want is a GUI for viewing the
stored data—a form with field names and values—and a way to fetch records by key.
It would also be useful to be able to update a record with new field values given its key
and to add new records from scratch by filling out the form.
'''

# Coding the GUI
"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this script runs on, as 1 or more local files;
"""
from tkinter import *
from tkinter.messagebox import showerror
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text="Fetch", command=fetchRecord).pack(side=LEFT) 
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]                                        # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]                                    # update existing record
    else:
        from person import Person                           # make/store new one for key
        record = Person(name='?', age='?')                  # make a new one
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()                                                  # back here after quit or window close

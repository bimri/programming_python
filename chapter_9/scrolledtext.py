"a simple text or file viewer component"

print('PP4E scrolledtext')
from tkinter import *

class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                        # make me expandable
        self.makewidgets()
        self.settext(text, file)
    
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                         # xlink sbar and text
        text.config(yscrollcommand=sbar.set)                    # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                           # pack first=clip last
        text.pack(side=LEFT, expand=YES, fill=BOTH)             # text clipped first
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                            # delete current text
        self.text.insert('1.0', text)                           # add at line 1, col 0
        self.text.mark_set(INSERT, '1.0')                       # set inset cursor
        self.text.focus()                                       # save user a click
    
    def gettext(self):                                          # returns a string
        return self.text.get('1.0', END+'-1c')                  # first through last
    


if __name__ == '__main__':
    import sys
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1])                     # filename on cmdline
    else:
        st = ScrolledText(text='Words\ngo here')                # or not: two lines
    def show(event):
        print(repr(st.gettext()))                               # show as raw string
    root.bind('<Key-Escape>', show)                             # esc = dump text
    root.mainloop()


'''
In all of these, the first argument is an absolute index that refers to the start of the text
string: string '1.0' means row 1, column 0 (rows are numbered from 1 and columns
from 0, though '0.0' is accepted as a reference to the start of the text, too). An index
'2.1' refers to the second character in the second row.
'''


"""
Like the listbox, text indexes can also be symbolic names: the END in the preceding
delete call refers to the position just past the last character in the text string (it’s a
tkinter variable preset to string 'end'). Similarly, the symbolic index INSERT (really,
string 'insert') refers to the position immediately after the insert cursor—the place
where characters would appear if typed at the keyboard. Symbolic names such as
INSERT can also be called marks.
"""

'''
For added precision, you can add simple arithmetic extensions to index strings. The
index expression END+'-1c' in the get call in the previous example, for instance, is really
the string 'end-1c' and refers to one character back from END. Because END points to
just beyond the last character in the text string, this expression refers to the last character
itself. The −1c extension effectively strips the trailing \n that this widget adds to
its contents (and which may add a blank line if saved in a file).
'''


"""
Similar index string extensions let you name characters ahead (+1c), name lines ahead
and behind (+2l, −2l), and specify things such as line ends and word starts around an
index (lineend, wordstart). Indexes show up in most Text widget calls.

Besides row/column identifier strings, you can also pass positions as names
of marks—symbolic names for a position between two characters. Unlike absolute row/
column positions, marks are virtual locations that move as new text is inserted or deleted
(by your script or your user). A mark always refers to its original location, even if
that location shifts to a different row and column over time.
"""


'''
Text marks. Besides row/column identifier strings, you can also pass positions as names
of marks—symbolic names for a position between two characters. Unlike absolute row/
column positions, marks are virtual locations that move as new text is inserted or deleted
(by your script or your user). A mark always refers to its original location, even if
that location shifts to a different row and column over time.

To create a mark, call the Text object’s mark_set method with a string name and an
index to give its logical location. For instance, this script sets the insert cursor at the
start of the text initially, with a call like the first one here:
    self.text.mark_set(INSERT, '1.0') # set insert cursor to start
    self.text.mark_set('linetwo', '2.0') # mark current line 2

The name INSERT is a predefined special mark that identifies the insert cursor position;
setting it changes the insert cursor’s location. To make a mark of your own, simply
provide a unique name as in the second call here and use it anywhere you need to specify
a text position. The mark_unset call deletes marks by name.
'''


"""
Text tags. In addition to absolute indexes and symbolic mark names, the Text widget
supports the notion of tags—symbolic names associated with one or more substrings
within the Text widget’s string. Tags can be used for many things, but they also serve
to represent a position anywhere you need one: tagged items are named by their beginning
and ending indexes, which can be later passed to position-based calls.

For example, tkinter provides a built-in tag name, SEL—a tkinter name preassigned to
string 'sel'—which automatically refers to currently selected text. To fetch the text
selected (highlighted) with a mouse, run either of these calls:
    text = self.text.get(SEL_FIRST, SEL_LAST) # use tags for from/to indexes
    text = self.text.get('sel.first', 'sel.last') # strings and constants work

The names SEL_FIRST and SEL_LAST are just preassigned variables in the tkinter module
that refer to the strings used in the second line here. The text get method expects two
indexes; to fetch text names by a tag, add .first and .last to the tag’s name to get its
start and end indexes.

To tag a substring, call the Text widget’s tag_add method with a tag name string and
start and stop positions (text can also be tagged as added in insert calls). To remove
a tag from all characters in a range of text, call tag_remove:

    self.text.tag_add('alltext', '1.0', END) # tag all text in the widget
    self.text.tag_add(SEL, index1, index2) # select from index1 up to index2
    self.text.tag_remove(SEL, '1.0', END) # remove selection from all text
"""


'''
The first line here creates a new tag that names all text in the widget—from start through
end positions. The second line adds a range of characters to the built-in SEL selection
tag—they are automatically highlighted, because this tag is predefined to configure its
members that way. The third line removes all characters in the text string from the
SEL tag (all selections are unselected). Note that the tag_remove call just untags text
within the named range; to really delete a tag completely, call tag_delete instead. Also
keep in mind that these calls apply to tags themselves; to delete actual text use the
delete method shown earlier.

You can map indexes to tags dynamically, too. For example, the text search method
returns the row.column index of the first occurrence of a string between start and stop
positions. To automatically select the text thus found, simply add its index to the builtin
SEL tag:
    where = self.text.search(target, INSERT, END) # search from insert cursor
    pastit = where + ('+%dc' % len(target)) # index beyond string found
    self.text.tag_add(SEL, where, pastit) # tag and select found string
    self.text.focus() # select text widget itself

If you want only one string to be selected, be sure to first run the tag_remove call listed
earlier—this code adds a selection in addition to any selections that already exist (it
may generate multiple selections in the display). In general, you can add any number
of substrings to a tag to process them as a group.

To summarize: indexes, marks, and tag locations can be used anytime you need a text
position. For instance, the text see method scrolls the display to make a position visible;
it accepts all three kinds of position specifiers:
    self.text.see('1.0') # scroll display to top
    self.text.see(INSERT) # scroll display to insert cursor mark
    self.text.see(SEL_FIRST) # scroll display to selection tag
'''

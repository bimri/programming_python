"""
file-like objects that save standard output text in a string and provide
standard input text from a string; redirect runs a passed-in function
with its output and input streams reset to these file-like class objects;
"""
import sys                                          # get built-in modules  


class Output:                                       # simulated output file
    def __init__(self):
        self.text = ''                              # empty string when created
    def write(self, string):                        # add a string of characters
        self.text += string
    def writelines(self, lines):                    # add each line in a list
        for line in lines: self.write(line)         # string or lines
    

class Input:
    def __init__(self, input=''):                   # default argument
        self.text = input                           # save string when created
    def read(self, size=None):                      # optional argument
        if size == None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
    def readline(self):
        eoln = self.text.find('\n')                 # find offset of next eoln
        if eoln == -1:                              # slice off through eoln
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res
    

def redirect(function, pargs, kargs, input):        # redirect stdin/out
    savestreams = sys.stdin, sys.stdout            # run a function object
    sys.stdin   = Input(input)                     # return stdout text
    sys.stdout  = Output()
    try:
        result = function(*pargs, **kargs)         # run function with args
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams        # restore if exc or not
    return (result, output)


''''
This module defines two classes that masquerade as real files:
    Output
        Provides the write method interface (a.k.a. protocol) expected of output files but
        saves all output in an in-memory string as it is written.
    Input
        Provides the interface expected of input files, but provides input on demand from
        an in-memory string passed in at object construction time.

The redirect function at the bottom of this file combines these two objects to run a
single function with input and output redirected entirely to Python class objects. The
passed-in function to run need not know or care that its print and input function calls
and stdin and stdout method calls are talking to a class rather than to a real file, pipe,
or user.
'''


"""
When run directly, the function reads from the keyboard and writes to the screen, just as if it were
run as a program without redirection:

C:\...\PP4E\System\Streams> python
>>> from teststreams import interact
>>> interact()
"""


'''
Now, let’s run this function under the control of the redirection function in
redirect.py and pass in some canned input text. In this mode, the interact function
takes its input from the string we pass in ('4\n5\n6\n'—three lines with explicit endof-
line characters), and the result of running the function is a tuple with its return value
plus a string containing all the text written to the standard output stream:
>>> from redirect import redirect
>>> (result, output) = redirect(interact, (), {}, '4\n5\n6\n')
>>> print(result)
>>> output
'''


"""
Better still, we can reuse the more.py module
it’s less to type and remember, and it’s already known to work well
>>> from PP4E.System.more import more
>>> more(output)
"""

'''
This is an artificial example, of course, but the techniques illustrated are widely applicable.
For instance, it’s straightforward to add a GUI interface to a program written to
interact with a command-line user. Simply intercept standard output with an object
such as the Output class instance shown earlier and throw the text string up in a window.
Similarly, standard input can be reset to an object that fetches text from a graphical
interface (e.g., a popped-up dialog box). Because classes are plug-and-play compatible
with real files, we can use them in any tool that expects a file.
'''

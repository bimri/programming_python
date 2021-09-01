"""
split and interactively page a string, file, or stream of
text to stdout; when run as a script, page stdin or file
whose name is passed on cmdline; if input is stdin, can't
use it for user reply--use platform-specific tools or GUI;
"""

import sys 

def getreply():
    """
    read a reply key from an interactive user
    even if stdin redirected to a file or pipe
    """
    if sys.stdin.isatty():                                      # if stdin is console
        return input('?')                                       # read reply line from stdin
    else:
        if sys.platform[:3] == 'win':                           # if stdin was redirected
            import msvcrt                                       # can't use to ask a user
            msvcrt.putch(b'?')
            key = msvcrt.getche()                               # use windows console tools
            msvcrt.putch(b'\n')                                 # getch() does not echo key
            return key
        else:
            assert False, 'platform not supported'
            #linux?: open('/dev/tty').readline()[:-1]
        
def more(text, numlines=10):
    """
    page multiline string to stdout
    """
    lines = text.splitlines()                                   # like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y']: break
    


if __name__ == '__main__':                                      # when run, not when imported
    if len(sys.argv) == 1:                                      # if no command-line arguments
        more(sys.stdin.read())                                  # page stdin, no inputs
    else:
        more(open(sys.argv[1]).read())                          # else page filename argument


'''
Most of the new code in this version shows up in its getreply function. The file’s
isatty method tells us whether stdin is connected to the console; if it is, we simply
read replies on stdin as before.
'''

"""
run with a command-line argument, this script interactively pages
through the named file’s text:

C:\...\PP4E\System\Streams> python moreplus.py adder.py
"""


"""
But now the script also correctly pages text redirected into stdin from either a file or a
command pipe, even if that text is too long to fit in a single display chunk.

C:\...\PP4E\System\Streams> python moreplus.py < moreplus.py
"""


"""
Finally, piping one Python script’s output into this script’s input now works as expected,

......\System\Streams> python teststreams.py < input.txt | python moreplus.py

Here, the standard output of one Python script is fed to the standard input of another
Python script located in the same directory: moreplus.py reads the output of
teststreams.py.
"""


'''
All of the redirections in such command lines work only because scripts don’t care what
standard input and output really are—interactive users, files, or pipes between programs.

We have just run this single more pager script in four
different ways: by importing and calling its function, by passing a filename commandline
argument, by redirecting stdin to a file, and by piping a command’s output to
stdin.
'''

"Other Redirection Options: os.popen and subprocess Revisited"
'''
the built-in os.popen function and its subprocess.Popen relative, 
which provide a way to redirect another command’s streams from 
within a Python program. these tools can be used to run a shell 
command line.

Other Redirection Options: os.popen and subprocess Revisited
Near the end of the preceding chapter, we took a first look at the built-in os.popen
function and its subprocess.Popen relative, which provide a way to redirect another
command’s streams from within a Python program. As we saw, these tools can be used
to run a shell command line (a string we would normally type at a DOS or csh prompt)
but also provide a Python file-like object connected to the command’s output stream—
reading the file object allows a script to read another program’s output. I suggested that
these tools may be used to tap into input streams as well.
Because of that, the os.popen and subprocess tools are another way to redirect streams
of spawned programs and are close cousins to some of the techniques we just met.
Their effect is much like the shell | command-line pipe syntax for redirecting streams
to programs (in fact, their names mean “pipe open”), but they are run within a script
and provide a file-like interface to piped streams. They are similar in spirit to the
redirect function, but are based on running programs (not calling functions), and the
command’s streams are processed in the spawning script as files (not tied to class objects).
These tools redirect the streams of a program that a script starts, instead of
redirecting the streams of the script itself.
'''

"Redirecting input or output with os.popen"
'''
In fact, by passing in the desired mode flag, we redirect either a spawned program’s
output or input streams to a file in the calling scripts, and we can obtain the spawned
program’s exit status code from the close method (None means “no error” here).

C:\...\PP4E\System\Streams> type hello-out.py
print('Hello shell world')

C:\...\PP4E\System\Streams> type hello-in.py
inp = input()
open('hello-in.txt', 'w').write('Hello ' + inp + '\n')
'''


'''
Python scripts can read output from other programs
and scripts like these, too, using code like the following:
C:\...\PP4E\System\Streams> python
>>> import os
>>> pipe = os.popen('python hello-out.py')                          # 'r' is default--read stdout
>>> pipe.read()

print(pipe.close())                                                 # exit status: None is good
'''


"""
But Python scripts can also provide input to spawned programs’ standard input
streams—passing a “w” mode argument, instead of the default “r”, connects the returned
object to the spawned program’s input stream. What we write on the spawning
end shows up as input in the program started:

>>> pipe = os.popen('python hello-in.py', 'w')                      # 'w'--write to program stdin
>>> pipe.write('Gumby\n')
>>> pipe.close()                                                    # \n at end is optional
>>> open('hello-in.txt').read()                                     # output sent to a file

The popen call is also smart enough to run the command string as an independent
process on platforms that support such a notion. It accepts an optional third argument
that can be used to control buffering of written text.
"""


"Redirecting input and output with subprocess"
'''
For even more control over the streams of spawned programs, we can employ the
subprocess module. module can emulate os.popen functionality, but it can also achieve feats such as
bidirectional stream communication (accessing both a program’s input and output)
and tying the output of one program to the input of another.

this module provides multiple ways to spawn a program and get both its
standard output text and exit status.

C:\...\PP4E\System\Streams> python
>>> from subprocess import Popen, PIPE, call
>>> X = call('python hello-out.py')                             # convenience
>>> X

>>> pipe = Popen('python hello-out.py', stdout=PIPE)
>>> pipe.communicate()[0]                                       # (stdout, stderr)
>>> pipe.returncode                                             # exit status

>>> pipe = Popen('python hello-out.py', stdout=PIPE)
>>> pipe.stdout.read()                                          # read all output
>>> pipe.wait()                                                 # exit status
'''

""" 
Redirecting and connecting to the spawned program’s input stream is just as simple,
though a bit more complex than the os.popen approach with 'w' file mode

>>> pipe = Popen('python hello-in.py', stdin=PIPE)
>>> pipe.stdin.write(b'Pokey\n')

>>> pipe.stdin.close()
>>> pipe.wait()

>>> open('hello-in.txt').read()                                 # output sent to a file


In fact, we can use obtain both the input and output streams of a spawned program with
this module.

C:\...\PP4E\System\Streams> type writer.py
print("Help! Help! I'm being repressed!")
print(42)

C:\...\PP4E\System\Streams> type reader.py
print('Got this: "%s"' % input())
import sys
data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data) * 2)
""" 


'''
the following connects two programs,
by piping the output of one Python script into another, first with shell syntax,
and then with the subprocess module:

C:\...\PP4E\System\Streams> python writer.py | python reader.py
Got this: "Help! Help! I'm being repressed!"
The meaning of life is 42 84
C:\...\PP4E\System\Streams> python
>>> from subprocess import Popen, PIPE
>>> p1 = Popen('python writer.py', stdout=PIPE)
>>> p2 = Popen('python reader.py', stdin=p1.stdout, stdout=PIPE)
>>> output = p2.communicate()[0]
>>> output
b'Got this: "Help! Help! I\'m being repressed!"\r\nThe meaning of life is 42 84\r\n'
>>> p2.returncode
0

We can get close to this with os.popen, but that the fact that its pipes are read or write
(and not both) prevents us from catching the second script’s output in our code:
>>> import os
>>> p1 = os.popen('python writer.py', 'r')
>>> p2 = os.popen('python reader.py', 'w')
>>> p2.write( p1.read() )
36
>>> X = p2.close()
Got this: "Help! Help! I'm being repressed!"
The meaning of life is 42 84
>>> print(X)
None
'''

"The subprocess module alternative"
'''
Python the subprocess module can achieve the same
effect as os.system and os.popen; it generally requires extra code but gives more control
over how streams are connected and used. This becomes especially useful when streams
are tied in more complex ways.
'''
import subprocess, os

os.chdir(r'E:\practice\programming_python\chapter_2')
print(os.getcwd())


print(subprocess.call('python sys_scripting.py'))                       # roughly like os.system()
print(subprocess.call('cmd /C str_mthd.py'))                            # built-in shell cmd

print(subprocess.call('type sys_scripting.py', shell=True))             # built-in shell cmd


"""
Notice the shell=True in the last command here. This is a subtle and platformdependent
requirement:
    • On Windows, we need to pass a shell=True argument to subprocess tools like
    call and Popen (shown ahead) in order to run commands built into the shell. Windows
    commands like “type” require this extra protocol, but normal executables
    like “python” do not.

    • On Unix-like platforms, when shell is False (its default), the program command
    line is run directly by os.execvp, a call we’ll meet in Chapter 5. If this argument is
    True, the command-line string is run through a shell instead, and you can specify
    the shell to use with additional arguments.
"""

'''
Besides imitating os.system, we can similarly use this module to emulate the
os.popen call used earlier, to run a shell command and obtain its standard output text
in our script:
'''
pipe = subprocess.Popen('python sys_scripting.py', stdout=subprocess.PIPE)
print(pipe.communicate())

'''
Here, we connect the stdout stream to a pipe, and communicate to run the command
to completion and receive its standard output and error streams’ text; the command’s
exit status is available in an attribute after it completes.

Alternatively, we can use other
interfaces to read the command’s standard output directly and wait for it to exit (which
returns the exit status):
'''
pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)
print(pipe.stdout.read())


'''
In fact, there are direct mappings from os.popen calls to subprocess.Popen objects:
    >>> from subprocess import Popen, PIPE
    >>> Popen('python helloshell.py', stdout=PIPE).communicate()[0]
    b'The Meaning of Life\r\n'
    >>>
    >>> import os
    >>> os.popen('python helloshell.py').read()
    'The Meaning of Life\n'
'''


"Shell command limitations"
'''
you should keep in mind two limitations of system and popen. First,
although these two functions themselves are fairly portable, their use is really only as
portable as the commands that they run.

Second, it is important to remember that running Python files as programs this way is
very different and generally much slower than importing program files and calling
functions they define. When os.system and os.popen are called, they must start a brandnew,
independent program running on your operating system

imported modules are a faster and more direct way to compose systems.

you should also know that the os.system call
normally blocks—that is, pauses—its caller until the spawned command line exits.


os.startfile call was added in recent Python releases.
This call opens a file with whatever program is listed in the Windows registry for the
file’s type—as though its icon has been clicked with the mouse cursor:
    os.startfile("webpage.html") # open file in your web browser
    os.startfile("document.doc") # open file in Microsoft Word
    os.startfile("myscript.py") # run file with Python
'''

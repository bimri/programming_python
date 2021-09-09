"Other Ways to Start Programs" 
'The os.startfile call on Windows'
'''
Although os.spawn calls may be largely superfluous today, there are other tools that
can still make a strong case for themselves. For instance, the os.system call can be used
on Windows to launch a DOS start command, which opens (i.e., runs) a file independently
based on its Windows filename associations, as though it were clicked.
os.startfile makes this even simpler in recent Python releases, and it can avoid blocking
its caller, unlike some other tools.
'''


'''
To understand why, first you need to know how the DOS start command works in
general. Roughly, a DOS command line of the form start command works as if command
were typed in the Windows Run dialog box available in the Start button menu. If
command is a filename, it is opened exactly as if its name was double-clicked in the
Windows Explorer file selector GUI.
'''


"""
For instance, the following three DOS commands automatically start Internet Explorer,
my registered image viewer program, and my sound media player program on the files
named in the commands. Windows simply opens the file with whatever program is
associated to handle filenames of that form. Moreover, all three of these programs run
independently of the DOS console box where the command is typed:

C:\...\PP4E\System\Media> start lp4e-preface-preview.html
C:\...\PP4E\System\Media> start ora-lp4e.jpg
C:\...\PP4E\System\Media> start sousa.au


Because the start command can run any file and command line, there is no reason it
cannot also be used to start an independently running Python program:
    C:\...\PP4E\System\Processes> start child.py 1
    
This works because Python is registered to open names ending in .py when it is installed.
The script child.py is launched independently of the DOS console window even though
we didn’t provide the name or path of the Python interpreter program. Because
child.py simply prints a message and exits, though, the result isn’t exactly satisfying: a
new DOS window pops up to serve as the script’s standard output, and it immediately
goes away when the child exits. To do better, add an input call at the bottom of the
program file to wait for a key press before exiting:
    C:\...\PP4E\System\Processes> type child-wait.py
    import os, sys
    print('Hello from child', os.getpid(), sys.argv[1])
    input("Press <Enter>") # don't flash on Windows
    
    C:\...\PP4E\System\Processes> start child-wait.py 2

Now the child’s DOS window pops up and stays up after the start command has
returned. Pressing the Enter key in the pop-up DOS window makes it go away.
"""


'Using start in Python scripts'
'''
Since we know that Python’s os.system and os.popen can be called by a script to run
any command line that can be typed at a DOS shell prompt, we can also start independently
running programs from a Python script by simply running a DOS start
command line. For instance:
    C:\...\PP4E\System\Media> python
    >>> import os
    >>> cmd = 'start lp4e-preface-preview.html' # start IE browser
    >>> os.system(cmd) # runs independent
    0
'''


'The os.startfile call'
'''
In fact, start is so useful that recent Python releases also include an os.startfile call,
which is essentially the same as spawning a DOS start command with os.system and
works as though the named file were double-clicked. The following calls, for instance,
have a similar effect:
    >>> os.startfile('lp-code-readme.txt')
    >>> os.system('start lp-code-readme.txt')

On recent versions of Windows, the following has a similar effect, too, because the
registry is used at the command line (though this form pauses until the file’s viewer is
closed—like using start /WAIT):
    >>> os.system('lp-code-readme.txt') # 'start' is optional today    

This is a convenient way to open arbitrary document and media files, but keep in mind
that the os.startfile call works only on Windows, because it uses the Windows registry
to know how to open a file.
'''

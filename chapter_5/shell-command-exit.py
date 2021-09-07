"Shell Command Exit Status Codes"
'''
Both the sys and os exit calls we just met accept an argument that denotes the exit
status code of the process(it’s optional in the sys call but required by os). After exit,
this code may be interrogated in shells and by programs that ran the script as a child
process.

On Linux, for example, we ask for the status shell variable’s value in order to
fetch the last program’s exit status; by convention, a nonzero status generally indicates
that some sort of problem occurred:

[mark@linux]$ python testexit_sys.py
Bye sys world
[mark@linux]$ echo $status
42
[mark@linux]$ python testexit_os.py
Bye os world
[mark@linux]$ echo $status
99
'''


"""
In a chain of command-line programs, exit statuses could be checked along the way as
a simple form of cross-program communication.

We can also grab hold of the exit status of a program run by another script. For instance,
as introduced in Chapters 2 and 3, when launching shell commands, exit status is
provided as:

    • The return value of an os.system call
    • The return value of the close method of an os.popen object (for historical reasons,
    None is returned if the exit status was 0, which means no error occurred)
    • A variety of interfaces in the subprocess module (e.g., the call function’s return
    value, a Popen object’s returnvalue attribute and wait method result)

In addition, when running programs by forking processes, the exit status is available
through the os.wait and os.waitpid calls in a parent process.
"""

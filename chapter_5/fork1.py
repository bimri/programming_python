"Forking Processes"
'''
Forked processes are a traditional way to structure parallel tasks, and they are a fundamental
part of the Unix tool set. Forking is a straightforward way to start an independent
program, whether it is different from the calling program or not. Forking is
based on the notion of copying programs: when a program calls the fork routine, the
operating system makes a new copy of that program and its process in memory and
starts running that copy in parallel with the original. Some systems don’t really copy
the original program (it’s an expensive operation), but the new copy works as if it were
a literal copy.

After a fork operation, the original copy of the program is called the parent process,
and the copy created by os.fork is called the child process. In general, parents can make
any number of children, and children can create child processes of their own; all forked
processes run independently and in parallel under the operating system’s control, and
children may continue to run after their parent exits.
'''

"forks child processes until you type 'q'"

import os

def child():
    print('A new child ',  os.getpid())
    os._exit(0)                                         # else goes back to parent loop


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Parent:', os.getpid(), newpid)
        if input() == 'q': break

parent()


'''
Python’s process forking tools, available in the os module, are simply thin wrappers
over standard forking calls in the system library also used by C language programs. To
start a new, parallel process, call the os.fork built-in function. Because this function
generates a copy of the calling program, it returns a different value in each copy: zero
in the child process and the process ID of the new child in the parent.
'''


"""
Because forking is ingrained in the Unix programming model, this script works well on
Unix, Linux, and modern Macs. Unfortunately, this script won’t work on the standard
version of Python for Windows today, because fork is too much at odds with the Windows
model. Python scripts can always spawn threads on Windows, and the multi
processing module.
"""
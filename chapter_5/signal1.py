"""
catch signals in Python; pass signal number N as a command-line arg,
use a "kill -N pid" shell command to send this process a signal; most
signal handlers restored by Python after caught (see network scripting
chapter for SIGCHLD details); on Windows, signal module is available,
but it defines only a few signal types there, and os.kill is missing;
"""

import sys, signal, time
def now(): return time.ctime(time.time())               # current time string

def onSignal(signum, stackframe):                       # signal handler
    print('Got signal', signum, 'at', now())            # most handlers stay in effect

signum = int(sys.argv[1])                               # signal number from cmd-line
signal.signal(signum, onSignal)                         # set signal handler; install handler
while True: signal.pause()                              # wait for signal


'''
There are only two signal module calls at work here:
signal.signal
    Takes a signal number and function object and installs that function to handle that
    signal number when it is raised. Python automatically restores most signal handlers
    when signals occur, so there is no need to recall this function within the signal
    handler itself to reregister the handler. That is, except for SIGCHLD, a signal handler
    remains installed until explicitly reset (e.g., by setting the handler to SIG_DFL to
    restore default behavior or to SIG_IGN to ignore the signal). SIGCHLD behavior is
    platform specific.
signal.pause
    Makes the process sleep until the next signal is caught. A time.sleep call is similar
    but doesn’t work with signals on my Linux box; it generates an interrupted system
    call error. A busy while True: pass loop here would pause the script, too, but may
    squander CPU resources.
'''

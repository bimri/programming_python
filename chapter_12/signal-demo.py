"Preventing zombies with signal handlers on Linux"
'''
On some systems, it’s also possible to clean up zombie child processes by resetting the
signal handler for the SIGCHLD signal delivered to a parent process by the operating
system when a child process stops or exits. If a Python script assigns the SIG_IGN (ignore)
action as the SIGCHLD signal handler, zombies will be removed automatically and immediately
by the operating system as child processes exit; the parent need not issue
wait calls to clean up after them. Because of that, this scheme is a simpler alternative
to manually reaping zombies on platforms where it is supported.

Python’s standard signal module lets scripts install handlers for signals—software-generated events.
'''


"""
Demo Python's signal module; pass signal number as a command-line arg, and use
a "kill -N pid" shell command to send this process a signal; on my Linux machine,
SIGUSR1=10, SIGUSR2=12, SIGCHLD=17, and SIGCHLD handler stays in effect even if
not restored: all other handlers are restored by Python after caught, but SIGCHLD
behavior is left to the platform's implementation; signal works on Windows too,
but defines only a few signal types; signals are not very portable in general;
"""
import sys, signal, time
def now():
    return time.asctime()
def onSignal(signum, stackframe):               # Python signal handler
    print('Got signal', signum, 'at', now())    # most handlers stay in effect
    if signum == signal.SIGCHLD:                # but sigchld handler is not
        print('sigchld caught')
        #signal.signal(signal.SIGCHLD, onSignal)

signum = int(sys.argv[1])
signal.signal(signum, onSignal)                 # install signal handler
while True: signal.pause()                      # sleep waiting for signals


# Signal numbers vary from machine to machine, so you should normally
# use their names, not their numbers. SIGCHLD behavior may vary per platform as well.


"""
Now, to apply all of this signal knowledge to killing zombies, simply set the SIGCHLD
signal handler to the SIG_IGN ignore handler action; on systems where this assignment
is supported, child processes will be cleaned up when they exit.
"""

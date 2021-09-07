"Program Exits"
'os Module Exits'
'''
It’s possible to exit Python in other ways, too. For instance, within a forked child process
on Unix, we typically call the os._exit function rather than sys.exit; threads may
exit with a _thread.exit call; and tkinter GUI applications often end by calling something
named Tk().quit().
'''

"""
On os._exit, the calling process exits immediately instead of raising an exception that
could be trapped and ignored. In fact, the process also exits without flushing output
stream buffers or running cleanup handlers (defined by the atexit standard library
module), so this generally should be used only by child processes after a fork, where
overall program shutdown actions aren’t desired.
"""

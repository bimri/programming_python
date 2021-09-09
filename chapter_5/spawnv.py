"""
start up 10 copies of child.py running in parallel;
use spawnv to launch a program on Windows (like fork+exec);
P_OVERLAY replaces, P_DETACH makes child stdout go nowhere;
or use portable subprocess or multiprocessing options today!
"""
import os, sys

for i in range(10):
    if sys.platform[:3] == 'win':
        pypath = sys.executable
        os.spawnv(os.P_NOWAIT, pypath, ('python', 'child.py', str(i)))
    else:
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            os.execlp('python', 'python', 'child.py', str(i))
print('Main process exiting.')


"""
In this script, we call os.spawnv with a process mode flag, the full
directory path to the Python interpreter, and a tuple of strings representing the shell
command line with which to start a new program.

The path to the Python interpreter executable program running a script is available as 
sys.executable. In general, the process mode flag is taken from these predefined values:
    os.P_NOWAIT and os.P_NOWAITO
        The spawn functions will return as soon as the new process has been created, with
        the process ID as the return value. Available on Unix and Windows.
    
    os.P_WAIT
        The spawn functions will not return until the new process has run to completion
        and will return the exit code of the process if the run is successful or “-signal” if a
        signal kills the process. Available on Unix and Windows.
    
    os.P_DETACH and os.P_OVERLAY
        P_DETACH is similar to P_NOWAIT, but the new process is detached from the console
        of the calling process. If P_OVERLAY is used, the current program will be replaced
        (much like os.exec). Available on Windows.


In fact, there are eight different calls in the spawn family, which all start a program but
vary slightly in their call signatures. In their names, an “l” means you list arguments
individually, “p” means the executable file is looked up on the system path, and “e”
means a dictionary is passed in to provide the shelled environment of the spawned
program: the os.spawnve call, for example, works the same way as os.spawnv but accepts
an extra fourth dictionary argument to specify a different shell environment for the
spawned program.

All the process mode flags are supported on Windows, but detach and
overlay modes are not available on Unix. Because this sort of detail may be prone to
change, to verify which are present, be sure to see the library manual or run a dir builtin
function call on the os module after an import.
"""

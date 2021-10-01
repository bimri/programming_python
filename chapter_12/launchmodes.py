"A Portable Program-Launch Framework"

"""
###################################################################################
launch Python programs with command lines and reusable launcher scheme classes;
auto inserts "python" and/or path to Python executable at front of command line;
some of this module may assume 'python' is on your system path (see Launcher.py);
subprocess module would work too, but os.popen() uses it internally, and the goal
is to start a program running independently here, not to connect to its streams;
multiprocessing module also is an option, but this is command-lines, not functions:
doesn't make sense to start a process which would just do one of the options here;
new in this edition: runs script filename path through normpath() to change any
/ to \ for Windows tools where required; fix is inherited by PyEdit and others;
on Windows, / is generally allowed for file opens, but not by all launcher tools;
###################################################################################
"""

import sys, os
pyfile = (sys.platform[:3] == 'win' and 'python.exe') or 'python'
pypath = sys.executable     # use sys in newer pys


def fixWindowsPath(commandline):
    """
    change all / to \ in script filename path at front of commandline ;
    used only by classes which run tools that require this on Windows;
    on other platforms, this does not hurt (e.g., os.system on Unix);
    """
    splitline = commandline.lstrip().split(' ')                     # split on spaces
    fixedpath = os.path.normpath(splitline[0])                  # fix forward slashes
    return ' '.join([fixedpath] + splitline[1:])                # put it back together


class LauchMode:
    """
    on call to instance, announce label and run command;
    subclasses format command lines as required in run();
    command should begin with name of the Python script
    file to run, and not with "python" or its full path;
    """
    def __init__(self, label, command):
        self.what = label
        self.where = command
    def __call__(self):                                         # on call, ex: button press callback
        self.announce(self.what)
        self.run(self.where)                                    # subclass must define run()
    def announce(self, text):                                   # subclasses may redefine announce()
        print(text)                                             # methods instead of if/elif logic
    def run(self, commandline):
        assert False, 'run must be defined by subclasses'
    


class System(LauchMode):
    """
    run Python script named in shell command line
    caveat: may block caller, unless & added on Unix
    """
    def run(self, commandline):
        commandline = fixWindowsPath(commandline)
        os.system('%s %s' % (pypath, commandline))
    


class Popen(LauchMode):
    """
    run shell command line in a new process
    caveat: may block caller, since pipe closed too soon
    """
    def run(self, commandline):
        commandline = fixWindowsPath(commandline)
        os.popen(pypath + ' ' + commandline)                        # assume nothing to be read
    


class Fork(LauchMode):
    """
    run command in explicitly created new process
    for Unix-like systems only, including cygwin
    """
    def run(self, commandline):
        assert hasattr(os, 'fork')
        commandline = commandline.split()                           # convert string to list
        if os.fork() == 0:                                          # start new child process
            os.execvp(pypath + [pyfile] + commandline)              # run new program in child
        
    

class Start(LauchMode):
    """
    run command independent of caller
    for Windows only: uses filename associations
    """
    def run(self, commandline):
        assert sys.platform[:3] == 'win'
        os.startfile('start' + commandline)                         # may create pop-up window
        
    

class Spawn(LauchMode):
    """
    run python in new process independent of caller
    for Windows or Unix; use P_NOWAIT for dos box;
    forward slashes are okay here
    """
    def run(self, commandline):
        os.spawnv(os.P_DETACH, pypath, (pyfile + commandline))
    


class Top_level(LauchMode):
    """
    run in new window, same process
    tbd: requires GUI class info too
    """
    def run(self, commandline):
        assert False, 'Sorry - mode not yet implemented'
    

#
# pick a "best" launcher for this platform
# may need to specialize the choice elsewhere
#

if sys.platform[:3] == 'win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork


class QuietPortableLauncher(PortableLauncher):
    def announce(self, text):
        pass



def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()                                      # no block

    input('system mode...')
    System(file, file)()                            # blocks

    if sys.platform[:3] == 'win':
        input('DOS start mode...')                  # no block
        Start(file, file)()


if __name__ == '__main__':
    selftest()



"""
To run a Python program, simply import the PortableLauncher class, make an instance
by passing a label and command line (without a leading “python” word), and then call
the instance object as though it were a function. The program is started by a call operation—
by its __call__ operator-overloading method, instead of a normally named
method—so that the classes in this module can also be used to generate callback handlers
in tkinter-based GUIs. As we’ll see in the upcoming chapters, button-presses in
tkinter invoke a callable object with no arguments; by registering a PortableLauncher
instance to handle the press event, we can automatically start a new program from
another program’s GUI. A GUI might associate a launcher with a GUI’s button press
with code like this:
    Button(root, text=name, command=PortableLauncher(name, commandLine))
"""

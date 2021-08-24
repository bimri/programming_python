"Script Execution Context"
“I’d Like to Have an Argument, Please”
'''
Python programs may have all sorts of enclosing
context—information automatically passed in to the program by the operating system
when the program starts up. For instance, scripts have access to the following sorts of
system-level inputs and interfaces:
    Current working directory
        os.getcwd gi ves access t o t he direct or y fr om whi ch a scri pt i s st art ed, and many fil e
        tools use its value implicitly.
    Command-line arguments
        sys.argv gives access to words typed on the command line that are used to start
        the program and that serve as script inputs.
    Shell variables
        os.environ provides an interface to names assigned in the enclosing shell (or a
        parent program) and passed in to the script.
    Standard streams
        sys.stdin, stdout, and stderr export t he t hree i nput/ out put strea ms t hat are at t he
        heart of command-line shell tools, and can be leveraged by scripts with print options,
        the os.popen call and subprocess module
'''

"CWD and Command Lines"
'''
This distinction between the CWD and import search paths explains why many scripts
in this book designed to operate in the current working directory (instead of one whose
name is passed in) are run with command lines such as this one:
    C:\temp> python C:\...\PP4E\Tools\cleanpyc.py process cwd

In this example, the Python script file itself lives in the directory C:\...\PP4E\Tools, but
because it is run from C:\temp, it processes the files located in C:\temp (i.e., in the CWD,
not in the script’s home directory). To process files elsewhere with such a script, simply
cd to the directory to be processed to change the CWD:
    C:\temp> cd C:\PP4thEd\Examples
    C:\PP4thEd\Examples> python C:\...\PP4E\Tools\cleanpyc.py process cwd

Because the CWD is always implied, a cd command tells the script which directory to
process in no less certain terms than passing a directory name to the script explicitly,
like this (portability note: you may need to add quotes around the *.py in this and other
command-line examples to prevent it from being expanded in some Unix shells):
    C:\...\PP4E\Tools> python find.py *.py C:\temp process named dir

In this command line, the CWD is the directory containing the script to be run (notice
that the script filename has no directory path prefix); but since this script processes a
directory named explicitly on the command line (C:\temp), the CWD is irrelevant. Finally,
if we want to run such a script located in some other directory in order to process
files located in yet another directory, we can simply give directory paths to both:
    C:\temp> python C:\...\PP4E\Tools\find.py *.cxx C:\PP4thEd\Examples\PP4E

Here, the script has import visibility to files in its PP4E\Tools home directory and processes
files in the directory named on the command line, but the CWD is something
else entirely (C:\temp). This last form is more to type, of course, but watch for a variety
of CWD and explicit script-path command lines like these in this book.
'''

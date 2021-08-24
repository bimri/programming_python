"Current Working Directory"
'''
The notion of the current working directory (CWD) turns out to be a key concept in
some scripts’ execution: it’s always the implicit place where files processed by the script
are assumed to reside unless their names have absolute directory paths.

Keep in mind, though, that filenames without full pathnames map to the CWD and
have nothing to do with your PYTHONPATH setting.

Technically, a script is always
launched from the CWD, not the directory containing the script file. Conversely, imports
always first search the directory containing the script, not the CWD (unless the
script happens to also be located in the CWD).
'''

'CWD, Files, and Import Paths'
'''
When you run a Python script by typing a shell command line such as python
dir1\dir2\file.py, the CWD is the directory you were in when you typed this command,
not dir1\dir2. 

On the other hand, Python automatically adds the identity of the
script’s home directory to the front of the module search path such that file.py can
always import other files in dir1\dir2 no matter where it is run from.
'''


""" 
Now, running this script in the directory in which it resides sets the CWD as expected
and adds it to the front of the module import search path.

    C:\...\PP4E\System> set PYTHONPATH=C:\PP4thEd\Examples
    C:\...\PP4E\System> python whereami.py
    my os.getcwd => C:\...\PP4E\System
    my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...more... ]
"""


'''
But if we run this script from other places, the CWD moves with us (it’s the directory
where we type commands), and Python adds a directory to the front of the module
search path that allows the script to still see files in its own home directory. For instance,
when running from one level up (..), the System name added to the front of sys.path
will be the first directory that Python searches for imports within whereami.py; it points
imports back to the directory containing the script that was run. Filenames without
complete paths, though, will be mapped to the CWD (C:\PP4thEd\Examples\PP4E),
not the System subdirectory nested there:
    C:\...\PP4E\System> cd ..
    C:\...\PP4E> python System\whereami.py
    my os.getcwd => C:\...\PP4E
    my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...more... ]
    C:\...\PP4E> cd System\temp
    C:\...\PP4E\System\temp> python ..\whereami.py
    my os.getcwd => C:\...\PP4E\System\temp
    my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...]

The net effect is that filenames without directory paths in a script will be mapped to
the place where the command was typed (os.getcwd), but imports still have access to
the directory of the script being run (via the front of sys.path). Finally, when a file is
launched by clicking its icon, the CWD is just the directory that contains the clicked
file. The following output, for example, appears in a new DOS console box when
whereami.py is double-clicked in Windows Explorer:
    my os.getcwd => C:\...\PP4E\System
    my sys.path => ['C:\\...\\PP4E\\System', ...more... ]
'''


"""
In this case, both the CWD used for filenames and the first import search directory are
the directory containing the script file. This all usually works out just as you expect,
but there are two pitfalls to avoid:
    • Filenames might need to include complete directory paths if scripts cannot be sure
    from where they will be run.

    • Command-line scripts cannot always rely on the CWD to gain import visibility to
    files that are not in their own directories; instead, use PYTHONPATH settings and
    package import paths to access modules in other directories.
"""


'''
For example, scripts in this book, regardless of how they are run, can always import
other files in their own home directories without package path imports (import file
here), but must go through the PP4E package root to find files anywhere else in the
examples tree (from PP4E.dir1.dir2 import filethere), even if they are run from the
directory containing the desired external module. 

As usual for modules, the PP4E
\dir1\dir2 directory name could also be added to PYTHONPATH to make files there visible
everywhere without package path imports (though adding more directories to PYTHON
PATH increases the likelihood of name clashes). In either case, though, imports are always
resolved to the script’s home directory or other Python search path settings, not
to the CWD.
'''

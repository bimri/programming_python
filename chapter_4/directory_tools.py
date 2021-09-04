"Directory Tools"
'''
One of the more common tasks in the shell utilities domain is applying an operation
to a set of files in a directory—a “folder” in Windows-speak. By running a script on a
batch of files, we can automate (that is, script) tasks we might have to otherwise run
repeatedly by hand.
'''

 
"Walking One Directory"
'''
The most common way to go about writing such tools is to first grab a list of the names
of the files you wish to process, and then step through that list with a Python for loop
or other iteration tool, processing each file in turn.

# how to get such a directory list within our scripts.

For scanning directories thereare at least three options: running shell listing commands with os.popen, matching
filename patterns with glob.glob, and getting directory listings with os.listdir. They
vary in interface, result format, and portability.
'''


"Running shell listing commands with os.popen"
'''
On Unix, directory listings are usually obtained by typing ls in a shell; on Windows,
they can be generated with a dir command typed in an MS-DOS console box. Because
Python scripts may use os.popen to run any command line that we can type in a shell
'''
# c:\temp> dir /B
# c:\temp> c:\cygwin\bin\ls
# c:\temp> c:\cygwin\bin\ls parts              # nested directory listings in 'parts'


"""
scripts can grab a listing of file and directory names at this level by simply
spawning the appropriate platform-specific command line and reading its output
"""
# E:\practice\programming_python\chapter_4> python
# >>> import os
# >>> os.popen('dir /B').readlines()
# ['binary-text_files.py\n', 'commands.py\n', 'data.txt\n', 'directory_tools.py\n', 'filetools.py\n', 'filters.py\n', 'hillbillies.txt\n', 'hillbillies.txt.out\n', 'inputfls.py\n', 'lower-level-filetools.py\n', 'os-open-modeflags.py\n', 'other-os-mod_filetools.py\n', 'scanfile.py\n', 'wrapping-descs.py\n', '__pycache__\n']

import os
for line in os.popen('dir /B'):                         # from my current working directory
    print(line[:-1])

lines = [line[:-1] for line in os.popen('dir /B')]
print(lines)


"""
For pipe objects, the effect of iterators may be even more useful than simply avoiding
loading the entire result into memory all at once: readlines will always block the caller
until the spawned program is completely finished, whereas the iterator might not.

The dir and ls commands let us be specific about filename patterns to be matched and
directory names to be listed by using name patterns;
"""
print(os.popen('dir /B').readlines())
# print(os.popen(r'c:\cygwin\bin\ls *.bin').readlines())
print(list(os.popen('dir chapter_4 /B')))
# print([fname in fname in popen(r'c:\cygwin\bin\ls chapter_3')])

'''
the downsides of os.popen are that it requires using a platform-specific shell command and
it incurs a performance hit to start up an independent program.
''' 

"Joining Files Portably"
#!/usr/bin/python
"""
################################################################################
join all part files in a dir created by split.py, to re-create file.
This is roughly like a 'cat fromdir/* > tofile' command on unix, but is
more portable and configurable, and exports the join operation as a
reusable function. Relies on sort order of filenames: must be same
length. Could extend split/join to pop up Tkinter file selectors.
################################################################################
"""

import os, sys 
readsize = 1024

def join(fromdir, tofile):
    output = open(tofile, 'wb')
    parts  = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj  = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile  = input('Name of file to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
    absfrom, absto = map(os.path.abspath, [fromdir, tofile])
    print('Joining', absfrom, 'to make', absto)
    
    try:
        join(fromdir, tofile)
    except:
        print('Error joining files:')
        print(sys.exc_info()[0], sys.exc_info()[1])
    else:
        print('Join complete: see', absto)
    if interactive: input('Press Enter key')                # pause if clicked


"""
Here is a join in progress on Windows, combining the split files we made a moment
ago; after running the join script, you still may need to run something like zip, gzip,
or tar to unpack an archive file unless it’s shipped as an executable,

C:\temp> python C:\...\PP4E\System\Filetools\join.py -help
Use: join.py [from-dir-name to-file-name]

C:\temp> python C:\...\PP4E\System\Filetools\join.py pysplit mypy31.msi
Joining C:\temp\pysplit to make C:\temp\mypy31.msi
Join complete: see C:\temp\mypy31.msi

C:\temp> dir *.msi

C:\temp> fc /b mypy31.msi python-3.1.msi
"""


'''
The join script simply uses os.listdir to collect all the part files in a directory created
by split, and sorts the filename list to put the parts back together in the correct order.
We get back an exact byte-for-byte copy of the original file (proved by the DOS fc
command in the code; use cmp on Unix).

Reading by blocks or files
    this script deals with files in binary mode but also reads each
    part file in blocks of 1 KB each. In fact, the readsize setting here (the size of each
    block read from an input part file) has no relation to chunksize in split.py.

    this script could instead
    read each part file all at once: output.write(open(filepath, 'rb').read()). The
    downside to this scheme is that it really does load all of a file into memory at once.

Sorting filenames
    the join scheme it
    uses relies completely on the sort order of filenames in the parts directory. Because
    it simply calls the list sort method on the filenames list returned by os.listdir, it
    implicitly requires that filenames have the same length and format when created
    by split. To satisfy this requirement, the splitter uses zero-padding notation in a
    string formatting expression ('part%04d') to make sure that filenames all have the
    same number of digits at the end (four). When sorted, the leading zero characters
    in small numbers guarantee that part files are ordered for joining correctly.
'''

"Splitting Files Portably"
#!/usr/bin/python
"""
################################################################################
split a file into a set of parts; join.py puts them back together;
this is a customizable version of the standard Unix split command-line
utility; because it is written in Python, it also works on Windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;
################################################################################
"""

import os, sys
kilobytes = 1024
megabytes = kilobytes * 1000
chucksize = int(1.4 * megabytes)                        # dedault: roughly a floppy

def split(fromfile, todir, chunksize=chucksize):
    if not os.path.exists(todir):                       # caller handles errors
        os.mkdir(todir)                                 # make dir, read/write parts
    else:
        for fname in os.listdir(todir):                 # delete any existing files
            os.remove(os.path.join(todir, fname))
    partnum = 0
    input = open(fromfile, 'rb')                        # binary: no decode, endline
    while True:                                         # eof-empty string from read
        chunk = input.read(chunksize)                   # get next part <= chunksize
        if not chunk: break 
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj  = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()                                 # or simplyu open().write()
    input.close()                                       
    assert partnum <= 9999                              # join sort fails if 5 digits
    return partnum
     

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split? ')      # input if clicked
            todir = input('Directory to store part files? ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]             # args in cmdline
            if len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)
        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished:', parts, 'parts are in', absto)
        if interactive: input('Press Enter key')        # pause if clicked



"""
C:\temp> cd C:\temp
C:\temp> dir python-3.1.msi

C:\temp> python C:\...\PP4E\System\Filetools\split.py -help
Use: split.py [file-to-split target-dir [chunksize]]

C:\temp> python C:\...\P4E\System\Filetools\split.py python-3.1.msi pysplit
Splitting C:\temp\python-3.1.msi to C:\temp\pysplit by 1433600
Split finished: 10 parts are in C:\temp\pysplit

C:\temp> dir pysplit
"""


'''
Operation modes
    This script is designed to input its parameters in either interactive or commandline
    mode; it checks the number of command-line arguments to find out the mode
    in which it is being used. In command-line mode, you list the file to be split and
    the output directory on the command line, and you can optionally override the
    default part file size with a third command-line argument.
    
    In interactive mode, the script asks for a filename and output directory at the console
    window with input and pauses for a key press at the end before exiting. This
    mode is nice when the program file is started by clicking on its icon; on Windows,
    parameters are typed into a pop-up DOS box that doesn’t automatically disappear.
    The script also shows the absolute paths of its parameters (by running them
    through os.path.abspath) because they may not be obvious in interactive mode.

Binary file mode
    on Windows, text-mode files automatically map
    \r\n end-of-line sequences to \n on input and map \n to \r\n on output. For true
    binary data, we really don’t want any \r characters in the data to go away when
    read, and we don’t want any superfluous \r characters to be added on output.
    Binary-mode files suppress this \r mapping when the script is run on Windows
    and so avoid data corruption.

Manually closing files    
    This script also goes out of its way to manually close its files. we can often get by 
    with a single line: open(partname, 'wb').write(chunk).
'''

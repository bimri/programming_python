"FTP get & put utilities" 
'Upload utilities'
'''
The upload interfaces in the FTP module are symmetric with the download interfaces.
Given a connected FTP object, its:
• storbinary method can be used to upload bytes from an open local file object
• storlines method can be used to upload text in ASCII mode from an open local
file object.

Unlike the download interfaces, both of these methods are passed a file object as a
whole, not a file object method (or other function).
'''

#!/usr/local/bin/python
"""
Store an arbitrary file by FTP in binary mode.  Uses anonymous
ftp unless you pass in a user=(name, pswd) tuple of arguments.
"""

import ftplib                    # socket-based FTP tools

def putfile(file, site, dir, user=(), *, verbose=True):
    """
    store a file by ftp to a site/directory
    anonymous or real login, binary transfer
    """
    if verbose: print('Uploading', file)
    local  = open(file, 'rb')               # local file of same name
    remote = ftplib.FTP(site)               # connect to FTP site
    remote.login(*user)                     # anonymous or real login
    remote.cwd(dir)
    remote.storbinary('STOR ' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose: print('Upload done.')

if __name__ == '__main__':
    site = 'ftp.rmi.net'
    dir  = '.'
    import sys, getpass
    pswd = getpass.getpass(site + ' pswd?')                # filename on cmdline
    putfile(sys.argv[1], site, dir, user=('lutz', pswd))   # nonanonymous login


'''
Notice that for portability, the local file is opened in rb binary input mode this time to
suppress automatic line-feed character conversions. If this is binary information, we
don’t want any bytes that happen to have the value of the \r carriage-return character
to mysteriously go away during the transfer when run on a Windows client.

We also
want to suppress Unicode encodings for nontext files, and we want reads to produce
the bytes strings expected by the storbinary upload operation.
'''

"""
This script uploads a file you name on the command line as a self-test, but you will
normally pass in real remote filename, site name, and directory name strings.
"""

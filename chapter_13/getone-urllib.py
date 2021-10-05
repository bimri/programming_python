"Using urllib to Download Files"
'''
Python urllib.request module: given an Internet address
string—a URL, or Universal Resource Locator—this module opens a connection
to the specified server and returns a file-like object ready to be read with normal file
object method calls (e.g., read, readline).

We can use such a higher-level interface to download anything with an address on the
Web—files published by FTP sites (using URLs that start with ftp://); web pages and
output of scripts that live on remote servers (using http:// URLs); and even local files
(using file:// URLs).
'''

#!/usr/local/bin/python
"""
A Python script to download a file by FTP by its URL string; use higher-level
urllib instead of ftplib to fetch file; urllib supports FTP, HTTP, client-side
HTTPS, and local files, and handles proxies, redirects, cookies, and more;
urllib also allows downloads of html pages, images, text, etc.; see also
Python html/xml parsers for web pages fetched by urllib in Chapter 19;
"""

import os, getpass
from urllib.request import urlopen                      # socket-based web tools

filename = 'monkeys.jpg'                                # remote/local filename
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://lutz:%s@ftp.rmi.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

# this works too:
# urllib.request.urlretrieve(remoteaddr, filename)

remotefile = urlopen(remoteaddr)                        # return input file-like object
localfile  = open(filename, 'wb')                       # where to store data locally
localfile.write(remotefile.read())
localfile.close()
remotefile.close()


'''
Technically speaking, urllib.request supports a variety of Internet protocols (HTTP,
FTP, and local files). Unlike ftplib, urllib.request is generally used for reading remote
objects, not for writing or uploading them (though the HTTP and FTP protocols support
file uploads too). As with ftplib, retrievals must generally be run in threads if
blocking is a concern.
'''

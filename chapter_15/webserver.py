"Running a Local Web Server"
'''
this script implements an HTTP web server,  which:
    • Listens for incoming socket requests from clients on the machine it is run on and
    the port number specified in the script or command line (which defaults to 80, that
    standard HTTP port)
    • Serves up HTML pages from the webdir directory specified in the script or command
    line (which defaults to the directory it is launched from)
    • Runs Python CGI scripts that are located in the cgi-bin (or htbin) subdirectory of
    the webdir directory, with a .py filename extension
'''


"""
Implement an HTTP web server in Python which knows how to serve HTML
pages and run server-side CGI scripts coded in Python; this is not
a production-grade server (e.g., no HTTPS, slow script launch/run on
some platforms), but suffices for testing, especially on localhost;
Serves files and scripts from the current working dir and port 80 by
default, unless these options are specified in command-line arguments;
Python CGI scripts must be stored in webdir\cgi-bin or webdir\htbin;
more than one of this server may be running on the same machine to serve
from different directories, as long as they listen on different ports;
"""

import os, sys 
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'        # where your HTML files & cgi-bin script directory live
port   = 80         # http://servername/ if 80, else use:servername:xxxx/

if len(sys.argv) > 1: webdir = sys.argv[1]              # command-line args
if len(sys.argv) > 2: port   = int(sys.argv[2])         # else default ., 80
print('webdir "%s", port %s' % (webdir, port))

os.chdir(webdir)                                        # run in HTML root dir
srvraddr = ('', port)                                   # my hostname, portnumber
srvrobbj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobbj.serve_forever()                                # serve clients till exit


'''
By default, while running locally this way, the script serves up HTML pages requested
on “localhost” from the directory it lives in or is launched from, and runs Python CGI
scripts from the cgi-bin subdirectory located there; change its webdir variable or pass
in a command-line argument to point it to a different directory. Because of this structure,
in the examples distribution HTML files are in the same directory as the web server
script and CGI scripts are located in the cgi-bin subdirectory. In other words, to visit
web pages and run scripts, we’ll be using URLs of these forms, respectively:
    http://localhost/somepage.html
    http://localhost/cgi-bin/somescript.py
'''

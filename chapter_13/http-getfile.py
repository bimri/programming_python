"HTTP: Accessing Websites"
'''
Python’s standard library (the modules that are installed with the interpreter) also includes
client-side support for HTTP—the Hypertext Transfer Protocol—a message
structure and port standard used to transfer information on the World Wide Web. In
short, this is the protocol that your web browser (e.g., Internet Explorer, Firefox,
Chrome, or Safari) uses to fetch web pages and run applications on remote servers as
you surf the Web. Essentially, it’s just bytes sent over port 80.
'''

"""
Python’s standard http.client module automates much of the protocol defined by
HTTP and allows scripts to fetch web pages as clients much like web browsers;
http.server also allows us to implement web servers to handle the
other side of the dialog.
"""


"""
fetch a file from an HTTP (web) server over sockets via http.client;  the filename
parameter may have a full directory path, and may name a CGI script with ? query
parameters on the end to invoke a remote program;  fetched file data or remote 
program output could be saved to a local file to mimic FTP, or parsed with str.find
or html.parser module;  also: http.client request(method, url, body=None, hdrs={});
"""

import sys, http.client
showlines = 6
try:
    servername, filename = sys.argv[1:]           # cmdline args?
except:
    servername, filename = 'learning-python.com', '/index.html'

print(servername, filename)
server = http.client.HTTPConnection(servername)   # connect to http site/server
server.putrequest('GET', filename)                # send request and headers
server.putheader('Accept', 'text/html')           # POST requests work here too
server.endheaders()                               # as do CGI script filenames

reply = server.getresponse()                      # read reply headers + data
if reply.status != 200:                           # 200 means success
    print('Error sending request', reply.status, reply.reason)
else:
    data = reply.readlines()                      # file obj for data received
    reply.close()                                 # show lines with eoln at end
    for line in data[:showlines]:                 # to save, write data to file
        print(line)                               # line already has \n, but bytes


'''
Desired server names and filenames can be passed on the command line to override
hardcoded defaults in the script.
'''

'''
Technically, the string we call filename in the script can refer to either a simple static
web page file or a server-side program that generates HTML as its output. Those serverside
programs are usually called CGI scripts. For
now, keep in mind that when filename refers to a script, this program can be used to
invoke another program that resides on a remote server machine. In that case, we can
also specify parameters (called a query string) to be passed to the remote program after
a ?.
'''

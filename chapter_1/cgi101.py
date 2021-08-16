#!/usr/bin/python
import cgi


form = cgi.FieldStorage()                               # parse form data
print('Content-type: text/html\n')                      # hdr plus blank line
print('<title>Reply Page</title>')                      # html reply page

if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i>!</h1>' % cgi.escape(form['user'].value))


'''
It uses the cgi module to parse the form’s input and insert it into the HTML
reply stream, properly escaped. The cgi module gives us a dictionary-like interface to
form inputs sent by the browser, and the HTML code that this script prints winds up
rendering the next page on the client’s browser. In the CGI world, the standard output
stream is connected to the client through a socket.
'''

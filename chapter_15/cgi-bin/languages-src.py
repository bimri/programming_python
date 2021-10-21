#!/usr/bin/python
"Display languages.py script code without running it."

import cgi
filename = 'cgi-bin/languages.py'

print('Content-type: text/html\n')          # wrap up in HTML
print('<TITLE>Languages</TITLE>')
print("<H1>Source code: '%s'</H1>" % filename)
print('<HR><PRE>')
print(cgi.escape(open(filename).read()))    # decode per platform default
print('</PRE><HR>')

"""
Note that here, too, it’s crucial to format the text of the file with cgi.escape, because
it is embedded in the HTML code of the reply. If we don’t, any characters in the text
that mean something in HTML code are interpreted as HTML tags.
"""

"SMTP Mail Sender Script"                       # Simple Mail Transfer Protocol

#!/usr/local/bin/python
"""
###########################################################################
use the Python SMTP mail interface module to send email messages; this
is just a simple one-shot send script--see pymail, PyMailGUI, and
PyMailCGI for clients with more user interaction features; also see
popmail.py for a script that retrieves mail, and the mailtools pkg
for attachments and formatting with the standard library email package;
###########################################################################
"""

import smtplib, sys, email.utils, mailconfig
mailserver = mailconfig.smtpservername         # ex: smtp.rmi.net

From = input('From? ').strip()                 # or import from mailconfig
To   = input('To?   ').strip()                 # ex: python-list@python.org
Tos  = To.split(';')                           # allow a list of recipients
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()                # curr datetime, rfc2822

# standard headers, followed by blank line, followed by text
text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line: 
        break                        # exit on ctrl-d/z
   #if line[:4] == 'From':
   #    line = '>' + line            # servers may escape
    text += line

print('Connecting...')
server = smtplib.SMTP(mailserver)              # connect, no log-in step
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:                                     # smtplib may raise exceptions
    print('Failed recipients:', failed)        # too, but let them pass here
else:
    print('No errors.')
print('Bye.')


'''
When you’re done, be sure to call the object’s quit method to disconnect from the
server and finalize the transaction. Notice that, on failure, the sendmail method may
either raise an exception or return a list of the recipient addresses that failed; the script
handles the latter case itself but lets exceptions kill the script with a Python error
message.

Subtly, calling the server object’s quit method after sendmail raises an exception may
or may not work as expected—quit can actually hang until a server timeout if the send
fails internally and leaves the interface in an unexpected state. For instance, this can
occur on Unicode encoding errors when translating the outgoing mail to bytes per the
ASCII scheme (the rset reset request hangs in this case, too). An alternative close
method simply closes the client’s sockets without attempting to send a quit command
to the server; quit calls close internally as a last step (assuming the quit command can
be sent!).
'''


"""
For advanced usage, SMTP objects provide additional calls not used in this example:
    • server.login(user, password) provides an interface to SMTP servers that require
    and support authentication.

    • server.starttls([keyfile[, certfile]]) puts the SMTP connection in Transport
    Layer Security (TLS) mode; all commands will be encrypted using the Python
    ssl module’s socket wrapper SSL support, and they assume the server supports
    this mode.
"""

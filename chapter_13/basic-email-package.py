"Basic email Package Interfaces in Action"

from email.message import Message
m = Message()
m['from'] = 'Hane Banks <hane@banks.com>'
m['to']   = 'PP4E@learning-python.com'
m.set_payload('The owls are not what they seem...')

s = str(m)
print(s); print();print('*' * 50)


# Parsing a message’s text—like the kind you obtain with poplib
'''
we get back a Message object from the text, 
with keys for headers and a payload for the body:
'''
from email.parser import Parser
x = Parser().parsestr(s) 
print(x)
print(); print('-' * 50)

print(x['From'])
print(x.get_payload())
print(x.items())
print('-' * 78)


'''
walk generator treats it as a single-part
mail, of type plain text:
'''
for part in x.walk():
    print(x.get_content_type())
    print(x.get_payload())


'Handling multipart messages'
from email.mime.multipart import MIMEMultipart              # Message subclasses
from email.mime.text import MIMEText                        # with extra headers+logic

top = MIMEMultipart()                                       # root Message object
top['from'] = 'Art <arthur@camelot.org>'                    # subtype default=mixed
top['to']   = 'PP4E@learning-python.com'

sub1 = MIMEText('nice red uniforms...\n')                   # part Message attachments
sub2 = MIMEText(open('data.txt').read())
sub2.add_header('Content-Disposition', 'attachment', filename='data.txt')
top.attach(sub1)
top.attach(sub2)

'''
When we ask for the text, a correctly formatted full mail 
text is returned, separators and all, ready to be sent with 
smtplib
'''
text = top.as_string()                                      # or do: str(top) or print(top)
print(text)


# message and retrieve it via poplib
'''
>>> text # same as in prior interaction
'Content-Type: multipart/mixed; boundary="===============1574823535=="\nMIME-Ver...'

>>> from email.parser import Parser
>>> msg = Parser().parsestr(text)
>>> msg['from']
'Art <arthur@camelot.org>'

>>> for part in msg.walk():
... print(part.get_content_type())
... print(part.get_payload())
... print()
...
multipart/mixed
[<email.message.Message object at 0x015EC610>,
<email.message.Message object at0x015EC630>]

text/plain
nice red uniforms...

text/plain
line1
line2
line3
'''
 
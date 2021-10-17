"NNTP: Accessing Newsgroups"

"""
fetch and print usenet newsgroup posting from comp.lang.python via the
nntplib module, which really runs on top of sockets; nntplib also supports
posting new messages, etc.; note: posts not deleted after they are read;
"""

listonly = False
showhdrs = ['From', 'Subject', 'Date', 'Newsgroups', 'Lines']
try:
    import sys
    servername, groupname, showcount = sys.argv[1:]
    showcount  = int(showcount)
except:
    servername = nntpconfig.servername       # assign this to your server
    groupname  = 'comp.lang.python'          # cmd line args or defaults
    showcount  = 10                          # show last showcount posts

# connect to nntp server
print('Connecting to', servername, 'for', groupname)
from nntplib import NNTP
connection = NNTP(servername)
(reply, count, first, last, name) = connection.group(groupname)
print('%s has %s articles: %s-%s' % (name, count, first, last))

# get request headers only
fetchfrom = str(int(last) - (showcount-1))
(reply, subjects) = connection.xhdr('subject', (fetchfrom + '-' + last))

# show headers, get message hdr+body
for (id, subj) in subjects:                  # [-showcount:] if fetch all hdrs
    print('Article %s [%s]' % (id, subj))
    if not listonly and input('=> Display?') in ['y', 'Y']:
        reply, num, tid, list = connection.head(id)
        for line in list:
            for prefix in showhdrs:
                if line[:len(prefix)] == prefix:
                    print(line[:80])
                    break
        if input('=> Show body?') in ['y', 'Y']:
            reply, num, tid, list = connection.body(id)
            for line in list:
                print(line[:80])
    print()
print(connection.quit())


'''
As for FTP and email tools, the script creates an NNTP object and calls its methods to
fetch newsgroup information and articles’ header and body text. The xhdr method, for
example, loads selected headers from a range of messages.

For NNTP servers that require authentication, you may also have to pass a username,
a password, and possibly a reader-mode flag to the NNTP call.
'''

'We could turn this script into a full-blown news interface'
# to post, say this (but only if you really want to post!)
connection = NNTP(servername)
localfile = open('filename') # file has proper headers
connection.post(localfile) # send text to newsgroup
connection.quit()

"Socket use cases"
'''
Despite their seemingly limited byte string nature, higher-order use
cases for sockets are not difficult to imagine. With a little extra work, for instance:
    • Arbitrary Python objects like lists and dictionaries (or at least copies of them) can
    be transferred over sockets, too, by shipping the serialized byte strings produced
    by Python’s pickle module

    • the printed output of a simple script can be redirected
    to a GUI window, by connecting the script’s output stream to a socket on which
    a GUI is listening in nonblocking mode.

    • the entire Internet can be seen as a socket use case. at the bottom, email, FTP, and web pages are largely just formatted byte
    string messages shipped over sockets.

Plus any other context in which programs exchange data—sockets are a general, portable,
and flexible tool.    
'''

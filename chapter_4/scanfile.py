"File Scanners"
'''
Unlike some shell-tool
languages, Python doesn’t have an implicit file-scanning loop procedure, but it’s simple
to write a general one that we can reuse for all time.
'''
def scanner(name, function):
    file = open(name, 'r')                      # create a file object
    while True:                                 
        line = file.readline()                  # call file methods
        if not line: break                      # until the end of the file
        function(line)                          # call a function object
    file.close()


"""
If we code this module
and put it in a directory on the module search path, we can use it any time we need to
step through a file line by line.
"""

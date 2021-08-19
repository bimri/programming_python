"Other String Concepts in Python 3.X: Unicode and bytes"
'''
Unicode also pops up today in the text displayed
in GUIs; the bytes shipped other networks; Internet standard such as email; and even
some persistence topics such as DBM files and shelves.
'''
# Unicode is no longer an optional topic for most Python 3.X programmers


'''
the following calls load a file’s
contents into a string, load a fixed-size set of bytes into a string, load a file’s contents
into a list of line strings, and load the next line in the file into a string, respectively:
    open('file').read()                         # read entire file into string
    open('file').read(N)                        # read next N bytes into string
    open('file').readlines()                    # read entire file into line strings list
    open('file').readline()                     # read next line, through '\n'

these calls can also be applied to shell commands in Python
to read their output. File objects also have write methods for sending strings to the
associated file.    
'''
file = open('spam.txt', 'w')                    # create file spam.txt
file.write(('spam' * 5) + '\n')                 # write text: returns #characters written
file.close()

file = open('spam.txt')                         # or open('spam.txt).read()
text = file.read()                              # read into a string
print(text)

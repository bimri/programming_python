"Binary and Text Files"
'''
Python scripts can also open
and process files containing binary data—JPEG images, audio clips, packed binary data
produced by FORTRAN and C programs, encoded text, and anything else that can be
stored in files as bytes.

The primary difference in terms of your code is the mode argument
passed to the built-in open function:
    >>> file = open('data.txt', 'wb') # open binary output file
    >>> file = open('data.txt', 'rb') # open binary input file
'''


"""
Strictly speaking, binary
mode disables Unicode encoding translation, but it also prevents the automatic endof-
line character translation performed by text-mode files by default.
"""


"End-of-line translations for text files"
'''
the end of a line of text in a file is represented by different characters
on different platforms. It’s a single \n character on Unix-like platforms, but the
two-character sequence \r\n on Windows.

For example, most Windows editors handle text in Unix format, but Notepad has been
a notable exception—text files copied from Unix or Linux may look like one long line
when viewed in Notepad, with strange characters inside (\n). Similarly, transferring a
file from Windows to Unix in binary mode retains the \r characters (which often appear
as ^M in text editors).

Python scripts that process text files don’t normally have to care, because the files object
automatically maps the DOS \r\n sequence to a single \n. It works like this by default—
when scripts are run on Windows:
    • For files opened in text mode, \r\n is translated to \n when input.
    • For files opened in text mode, \n is translated to \r\n when output.
    • For files opened in binary mode, no translation occurs on input or output.
'''


"""
Using binary mode avoids Unicode errors,
and automatically disables line-end translations

the fact that binary mode prevents end-of-line translations
to protect file content is best noted as a separate feature,

writing data in binary mode prevents all translations as expected, even if
the data happens to contain bytes that are part of line-ends in text mode

But reading binary data in text mode, whether accidental or not, can corrupt the data
when transferred because of line-end translations

The short story to remember here is that you should generally use \n to refer to endline
in all your text file content, and you should always open binary data in binary file
modes to suppress both end-of-line translations and any Unicode encodings.
"""


"Parsing packed binary data with the struct module"
# struct module provides calls to pack and unpack binary data
'''
It is also capable of composing and
decomposing using any endian-ness you desire (endian-ness determines whether the
most significant bits of binary numbers are on the left or right side).

>>> import struct
>>> data = struct.pack('>i4shf', 2, 'spam', 3, 1.234)
>>> data
b'\x00\x00\x00\x02spam\x00\x03?\x9d\xf3\xb6'
>>> file = open('data.bin', 'wb')
>>> file.write(data)
14
>>> file.close()

>>> file = open('data.bin', 'rb')
>>> bytes = file.read()
>>> values = struct.unpack('>i4shf', data)
>>> values
(2, b'spam', 3, 1.2339999675750732)
'''


"""
Packed binary data crops up in many contexts, including some networking tasks, and
in data produced by other programming languages.
"""


"Random access files"
'''
Binary files also typically see action in random access processing.
adding a + to the open mode string allows a file to be both read and written.
This mode is typically used in conjunction with the file object’s seek method to support
random read/write access.
'''
records = [bytes([char] * 8) for char in b'spam']
print(records)

file = open('randon.bin', 'w+b')
for rec in records:                                         # write four records
    size = file.write(rec)

file.flush()
print(file.seek(0))                                         # go to the start
print(file.read())                                          # read entire file


file = open('random.bin', 'r+b')
print(file.read(4))                                         # read the first record

record = b'X' * 8
file.seek(0)                                                # go to the start
file.write(record)                                          # write a record
file.seek(len(record) * 2)                                  # update third record
file.write(b'Y' * 8)

file.seek(8)
print(file.read(8))
file.read(len(record))                                      # fetch second record
file.seek(-8, 2)                                            # seek from the end
print(file.read(8))
file.seek(0)                                                # go to the start

# c:\temp> type random.bin                                  # the view outside Python

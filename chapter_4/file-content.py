"Unicode policies: File content versus file names"
'''
In fact, it’s important to keep in mind that there are two different Unicode concepts
related to files: the encoding of file content and the encoding of file name. Python provides
your platform’s defaults for these settings in two different attributes; on
Windows 7:
'''
import sys
print(sys.getfilesystemencoding())              # file name encoding, platform scheme
print(sys.getdefaultencoding())                 # file content encoding, platform default
print(sys.getfilesystemencodeerrors())


"""
These settings allow you to be explicit when needed—the content encoding is used
when data is read and written to the file, and the name encoding is used when dealing
with names prior to transferring data. In addition, using bytes for file name tools may
work around incompatibilities with the underlying file system’s scheme,

opening text files in binary mode may also mean that the raw
and still-encoded text will not match search strings as expected: search strings must
also be byte strings encoded per a specific and possibly incompatible encoding scheme.

On the other hand,
opening text in binary mode to suppress Unicode content decoding and avoid decoding
errors might still be useful if you do not wish to skip undecodable files and content is
largely irrelevant.
"""


'''
As a rule of thumb, you should try to always provide an encoding name for text content
if it might be outside the platform default, and you should rely on the default Unicode
API for file names in most cases.
'''

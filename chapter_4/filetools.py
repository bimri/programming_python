'''
In Python, the built-in open function is the primary tool scripts use to access the files
on the underlying computer system. When called, the open
function returns a new file object that is connected to the external file; the file object
has methods that transfer data to and from the file and perform a variety of file-related
operations. The open function also provides a portable interface to the underlying filesystem—
it works the same way on every platform on which Python runs.

Other file-related modules built into Python allow us to do things such as manipulate
lower-level descriptor-based files (os); copy, remove, and move files and collections of
files (os and shutil); store data and objects in files by key (dbm and shelve); and access
SQL databases (sqlite3 and third-party add-ons).
'''


"The File Object Model in Python 3.X"
'''
    • Text files contain Unicode text. In your script, text file content is always a str
    string—a sequence of characters (technically, Unicode “code points”). Text files
    perform the automatic line-end translations described in this chapter by default
    and automatically apply Unicode encodings to file content: they encode to and
    decode from raw binary bytes on transfers to and from the file, according to a
    provided or default encoding name. Encoding is trivial for ASCII text, but may be
    sophisticated in other cases.

    • Binary files contain raw 8-bit bytes. In your script, binary file content is always a
    byte string, usually a bytes object—a sequence of small integers, which supports
    most str operations and displays as ASCII characters whenever possible. Binary
    files perform no translations of data when it is transferred to and from files: no lineend
    translations or Unicode encodings are performed.

In practice, text files are used for all truly text-related data, and binary files store items
like packed binary data, images, audio files, executables, and so on.
'''


"Using Built-in File Objects"
'''
The open built-in function and its files objects are all
you need to remember to process files in your scripts. The file object returned by
open has methods for reading data (read, readline, readlines); writing data (write,
writelines); freeing system resources (close); moving to arbitrary positions in the file
(seek); forcing data in output buffers to be transferred to disk (flush); fetching the
underlying file handle (fileno); and more.
'''

'Output files'
'''
To make a new file, call open with two arguments: the external name of the file to be
created and a mode string w (short for write).

To store data on the file, call the file object’s
write method with a string containing the data to store, and then call the close method
to close the file.File write calls return the number of characters or bytes written
'''
file = open('mydata.txt', 'w')                            # open output file object: create if file doesn’t exist, truncate if it does

print(
    file.write('Hello, world!\n'),                           # writes strings verbatim to file
    file.write('This is our new text file\n'),
    file.write('and this is another line.\n'),             # returns number chars/bytes written
    file.write('Why? Because we can.\n')
)

file.close()

'''
Opening. In the open function call shown in the preceding example, the first argument
can optionally specify a complete directory path as part of the filename string. If we
pass just a simple filename without a path, the file will appear in Python’s current
working directory.

C:\temp> dir data.txt /B
C:\temp> type data.txt
'''

"""
Also note that when opening in w mode, Python either creates the external file if it does
not yet exist or erases the file’s current contents if it is already present on your machine
"""


'''
Writing. Notice that we added an explicit \n end-of-line character to lines written to the
file; unlike the print built-in function, file object write methods write exactly what they
are passed without adding any extra formatting.
'''

"""
Output files also sport a writelines method, which simply writes all of the strings in a
list one at a time without adding any extra formatting.

file.writelines(['Hello file world!\n', 'Bye file world.\n'])
"""


'''
Closing. The file close method used earlier finalizes file contents and frees up system
resources. For instance, closing forces buffered output data to be flushed out to disk.
Normally, files are automatically closed when the file object is garbage collected by the
interpreter (that is, when it is no longer referenced).

This includes all remaining open
files when the Python session or program exits. Because of that, close calls are often
optional. In fact, it’s common to see file-processing code in Python in this idiom:

    open('somefile.txt', 'w').write("G'day Bruce\n") # write to temporary object
    open('somefile.txt', 'r').read() # read from temporary object

Since both these expressions make a temporary file object, use it immediately, and do
not save a reference to it, the file object is reclaimed right after data is transferred, and
is automatically closed in the process. There is usually no need for such code to call the
close method explicitly.    

Mmanual close calls are not a bad idea in nontrivial programs, even if
they are technically not required. Closing is a generally harmless but robust habit to
form.
'''
 

"Ensuring file closure: Exception handlers and context managers"
'''
Manual file close method calls are easy in straight-line code, but how do you ensure
file closure when exceptions might kick your program beyond the point where the close
call is coded? First of all, make sure you must—files close themselves when they are
collected, and this will happen eventually, even when exceptions occur.

If closure is required, though, there are two basic alternatives: the try statement’s
finally clause is the most general, since it allows you to provide general exit actions
for any type of exceptions:
    myfile = open(filename, 'w')
    try:
        ...process myfile...
    finally:
        myfile.close()

In recent Python releases, though, the with statement provides a more concise alternative
for some specific objects and exit actions, including closing files:
    with open(filename, 'w') as myfile:
        ...process myfile, auto-closed on statement exit...        

In Python 3.1 and later, this statement can also specify multiple (a.k.a. nested) context
managers—any number of context manager items may be separated by commas, and
multiple items work the same as nested with statements. In general terms, the 3.1 and
later code:
    with A() as a, B() as b:
        ...statements...        

For example, when the with statement block exits in the following, both files’ exit
actions are automatically run to close the files, regardless of exception outcomes:
    with open('data') as fin, open('results', 'w') as fout:
        for line in fin:
            fout.write(transform(line))
'''

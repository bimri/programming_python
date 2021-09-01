"Chaining programs with pipes"
'''
On Windows and Unix-like platforms, it’s also possible to send the standard output
of one program to the standard input of another using the | shell character between
two commands.

This is usually called a “pipe” operation because the shell creates a
pipeline that connects the output and input of two commands.
'''
# C:\...\PP4E\System\Streams> python teststreams.py < input.txt | more

"""
Here, teststreams’s standard input comes from a file again, but its output (written by
print calls) is sent to another program, not to a file or window. The receiving program
is more, a standard command-line paging program available on Windows and Unix-like
platforms.
"""
# One Python script’s output can always be piped into another Python script’s input:
# "python writer.py | python reader.py"

'''
This time, two Python programs are connected. Script reader gets input from script
writer; both scripts simply read and write, oblivious to stream mechanics. In practice,
such chaining of programs is a simple form of cross-program communications. It makes
it easy to reuse utilities written to communicate via stdin and stdout in ways we never
anticipated. For instance, a Python program that sorts stdin text could be applied to
any data source we like, including the output of other scripts.
'''
 

""" 
C:\...\PP4E\System\Streams> type data.txt
C:\...\PP4E\System\Streams> python sorter.py < data.txt             sort a file
C:\...\PP4E\System\Streams> python adder.py < data.txt              sum file    add a file
C:\...\PP4E\System\Streams> type data.txt | python adder.py         sum type output.txt
C:\...\PP4E\System\Streams> type writer2.py
C:\...\PP4E\System\Streams> python writer2.py | python sorter.py    sort py output
C:\...\PP4E\System\Streams> writer2.py | sorter.py                  shorter form
C:\...\PP4E\System\Streams> python writer2.py | python sorter.py | python adder.py
"""

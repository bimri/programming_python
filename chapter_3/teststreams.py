"Redirecting Streams to Files and Programs"
'''
standard output (and print) text appears in the console window where a
program was started, standard input (and input) text comes from the keyboard, and
standard error text is used to print Python error messages to the console window.

Redirection is useful for things like canned (precoded) test inputs: we can apply a single
test script to any set of inputs by simply redirecting the standard input stream to a
different file each time the script is run.

Similarly, redirecting the standard output stream lets us save and later analyze a program’s 
output; for example, testing systems might compare the saved standard output of a script with 
a file of expected output to detect failures.
'''

"read numbers till eof and show squares"

def interact():
    print('Hello stream world')                             # print sends to sys.stdout
    while True:
        try:
            reply = input('Enter a number>')                # input reads sys.stdin
        except EOFError:
            break                                           # raises an except on eof
        else:                                               # input given as a string
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()                                              # when run, not imported


"""
# the input.txt file automates the input we would normally type interactively
    C:\...\PP4E\System\Streams> type input.txt
        8
        6

    C:\...\PP4E\System\Streams> python teststreams.py < input.txt
        Hello stream world
"""


'''
Standard output can be similarly
redirected to go to a file with the > filename shell syntax. In fact, we can combine
input and output redirection in a single command:
    C:\...\PP4E\System\Streams> python teststreams.py < input.txt > output.txt
'''

"Standard Streams"
'''
The sys module is also the place where the standard input, output, and error streams
of your Python programs live; these turn out to be another common way for programs
to communicate:
'''
import sys

for f in (sys.stdin, sys.stdout, sys.stderr): 
    '''
    The standard streams are simply preopened Python file objects that are automatically
    connected to your program’s standard streams when Python starts up.
    By default, all of them are tied to the console window where Python was started.
    '''
    print(f)

print(sys.stdout.write('hello stdout world' + '\n'))
print(input('hello stdin world>'))
print('hello stdin world>'); sys.stdin.readline()[:-1]

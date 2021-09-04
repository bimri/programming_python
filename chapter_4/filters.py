import sys 

def filter_files(name, function):                   # filter file through a function
    input = open(name, 'r')                         # create file objects
    output = open(name + '.out', 'w')               # explicit output file too

    # with open(name, 'r') as input, open(name + '.out', 'w') as output:
    for line in input:
        output.write(function(line))                # write the modified line
    input.close()
    output.close()                                  # output has a '.out' suffix


def filter_stream(function):                        # no explicit output files
    while True:                                     # use standard streams
        line = sys.stdin.readline()                 # or: input()
        if not line: break

        # line iterator
        # for line in sys.stdin:                    # read by lines automatically
        print(function(line), end='')               # or: sys.stdout.write()
    

if __name__ == '__main__':
    filter_stream(lambda line: line)                 # copy stdin to stdout if run

# C:\...\PP4E\System\Filetools> filters.py < hillbillies.txt
'''
But this module is also useful when imported as a library (clients provide the lineprocessing
function):
>>> from filters import filter_files
>>> filter_files('hillbillies.txt', str.upper)
>>> print(open('hillbillies.txt.out').read())
'''

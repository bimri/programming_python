import sys 
sum = 0
while True:
    try:
        line = input()                      # or call sys.stdin.readline()
    except EOFError:                        # or for line in sys.stdin:
        break                               # input strips \n at end
    else:
        sum += int(line)                    # was sting.atoi() in 2nd ed
print(sum)


'''
We can apply such general-purpose tools in a variety of ways at the shell command line
to sort and sum arbitrary files and program outputs
'''

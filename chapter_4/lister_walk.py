"list file tree with os.walk"

import sys, os

def lister(root):                                                   # for a root dir
    for (thisdir, subshere, fileshere) in os.walk(root):            # generate dirs in tree
        print('[' + thisdir + ']')
        for fname in fileshere:                                     # print files in this dir       
            path = os.path.join(thisdir, fname)                     # add dir name prefix
            print(path)
        
    

if __name__ == '__main__':
    lister(sys.argv[1])                                              # dirname from cmdline


# C:\...\PP4E\System\Filetools> python lister_walk.py C:\temp\test

'''
For instance, it supports
bottom-up instead of top-down walks with its optional topdown=False argument,
and callers may prune tree branches by deleting names in the subdirectories lists of the
yielded tuples.
'''
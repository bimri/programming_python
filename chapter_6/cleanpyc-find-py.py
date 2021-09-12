"""
find and delete all "*.pyc" bytecode files at and below the directory
named on the command-line; this uses a Python-coded find utility, and
so is portable; run this to delete .pyc's from an old Python release;
"""

import os, sys, find                                    # here, gets Tools.find

count = 0
for filename in find.find('*.pyc', sys.argv[1]):
    count += 1
    print(filename)
    os.remove(filename)

print('Removed %d .pyc files' % count)


'''
This works portably, and it avoids external program startup costs. But find is really
just half the story—it collects files matching a name pattern but doesn’t search their
content. Although extra code can add such searching to a find’s result, a more manual
approach can allow us to tap into the search process more directly.
'''

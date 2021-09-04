"Splitting and joining listing results"
'''
glob returns names with directory paths, whereas
listdir gives raw base filenames

For convenient processing, scripts often need to split
glob results into base files or expand listdir results into full paths.

Such translations
are easy if we let the os.path module do all the work for us. For example, a script that
intends to copy all files elsewhere will typically need to first split off the base filenames
from glob results so that it can add different directory names on the front:
'''

dirname = r'E:\practice\programming_python'

import glob, os

for file in glob.glob(dirname + '/*'):
    '''
    the names after the => represent names 
    that files might be moved to
    '''
    head, tail = os.path.split(file)
    print(head, tail, '=>', ('E:\\Other\\' + tail))
print('-'*80);print()

'''
a script that means to process all files in a different directory than the one it runs in will
probably need to prepend listdir results with the target directory name before passing
filenames on to other tools:
''' 

for file in os.listdir(dirname):
    print(dirname, file, '=>', os.path.join(dirname, file))


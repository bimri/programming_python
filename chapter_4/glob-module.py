"The glob module"
'''
The term globbing comes from the * wildcard character in filename patterns; per computing
folklore, a * matches a “glob” of characters. In less poetic terms, globbing simply
means collecting the names of all entries in a directory—files and subdirectories—
whose names match a given filename pattern.

glob.glob built-in—a tool that accepts a filename pattern to expand, and returns a list 
(not a generator) of matching file names:
'''
import glob 
print(glob.glob('*.py'))
print(glob.glob('*.bin'))
print(glob.glob('parts'))
print(glob.glob('parts/*'))
print(glob.glob('parts\part*'))
 

'''
The glob call accepts the usual filename pattern syntax used in shells: ? means any one
character, * means any number of characters, and [] is a character selection set.‡ The
pattern should include a directory path if you wish to glob in something other than the
current working directory, and the module accepts either Unix or DOS-style directory
separators (/ or \). This call is implemented without spawning a shell command (it uses
os.listdir.

glob is a bit more powerful. using it to list files in one directory is just one use of 
its pattern-matching skills. It can also be used to collect matching names across multiple 
directories, simply because each level in a passed-in directory path can be a pattern too:

# glob just uses the standard fnmatch module to match name patterns
'''

# Here, we get back filenames from 3 different directories that match the s*.py pattern
for path in glob.glob(r'E:\practice\programming_python\*\s*.py'):
    print(path)

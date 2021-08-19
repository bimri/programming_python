"The Loaded Modules Table"
'''
The sys module also contains hooks into the interpreter; sys.modules, for example, is
a dictionary containing one name:module entry for every module imported in your
Python session or program (really, in the calling Python process):
'''
import sys


print(sys.modules)
print(list(sys.modules.keys()))

print(sys)
print(sys.modules['sys'])


'''
We might use such a hook to write programs that display or otherwise process all the
modules loaded by a program (just iterate over the keys of sys.modules).
'''


"""
Also in the interpret hooks category, an object’s reference count is available via
sys.getrefcount, and the names of modules built-in to the Python executable are listed
in sys.builtin_module_names.
""" 

"System Scripting Overview"
import sys, os
print(sys.platform)

print(os.name)
print(os.getenv('PATH'))
print(os.getcwd())
# print(os.urandom(25))

print(len(dir(os)))
print(len(dir(sys)))
print(len(dir(os.path)))

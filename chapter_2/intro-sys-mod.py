"Introducing the sys Module"
import sys 
print(sys.platform)
print(sys.maxsize)
print(sys.version)


if sys.platform[:3] == 'win': print('hello windows')

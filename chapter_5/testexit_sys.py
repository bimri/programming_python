def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')


if __name__ == '__main__':
    later()


"""
Running this program as a script causes it to exit before the interpreter falls off the end
of the file. But because sys.exit raises a Python exception, importers of its function
can trap and override its exit exception or specify a finally cleanup block to be run
during program exit processing:
    >>> try:
        ... later()
    ... finally:
        ... print('Cleanup')
    ...
    Bye sys world
    Cleanup
"""
 
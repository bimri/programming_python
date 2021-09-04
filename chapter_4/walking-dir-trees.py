"Walking Directory Trees"
'''
You may have noticed that almost all of the techniques in this section so far return the
names of files in only a single directory (globbing with more involved patterns is the
only exception). That’s fine for many tasks, but what if you want to apply an operation
to every file in every directory and subdirectory in an entire directory tree?

For instance, suppose again that we need to find every occurrence of a global name in
our Python scripts. This time, though, our scripts are arranged into a module package:
a directory with nested subdirectories, which may have subdirectories of their own.
We could rerun our hypothetical single-directory searcher manually in every directory
in the tree, but that’s tedious, error prone, and just plain not fun.

Luckily, in Python it’s almost as easy to process a directory tree as it is to inspect a single
directory. We can either write a recursive routine to traverse the tree, or use a treewalker
utility built into the os module. Such tools can be used to search, copy, compare,
and otherwise process arbitrary directory trees on any platform that Python runs on
(and that’s just about everywhere).
'''

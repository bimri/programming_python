"Adding a GUI As a Separate Program: Command Pipes"
# GUI reader side: route spawned program standard output to a GUI window

from chapter_10.guiStreams import redirectedGuiShellCmd         # uses GuiOutput
redirectedGuiShellCmd('python -u pipe-nongui.py')               # -u: unbuffered


'''
Notice the -u Python command-line flag used here: it forces the spawned program’s
standard streams to be unbuffered, so we get printed text immediately as it is produced,
instead of waiting for the spawned program to completely finish.
'''

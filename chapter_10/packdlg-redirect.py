"Using Redirection for the Packing Scripts"
# wrap command-line script in GUI redirection tool to pop up its output

from tkinter import *
from packdlg import runPackDialog
from chapter_10.guiStreams import redirectedGuiFunc

def runPackDialog_Wrapped():                    # callback to run mytools.py
    redirectedGuiFunc(runPackDialog)            # wrap entire callback handler


if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)

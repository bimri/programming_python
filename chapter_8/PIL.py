"Viewing and Processing Images with PIL"
'''
Python tkinter scripts show images by associating independently
created image objects with real widget objects. At this writing, tkinter GUIs can display
photo image files in GIF, PPM, and PGM formats by creating a PhotoImage object, as
well as X11-style bitmap files (usually suffixed with an .xbm extension) by creating a
BitmapImage object.

This set of supported file formats is limited by the underlying Tk library, not by tkinter.
you can either convert your files to one of the supported formats with an image-processing 
program or install the PIL Python extension package.

PIL, the Python Imaging Library, is an open source system that supports nearly 30
graphics file formats (including GIF, JPEG, TIFF, PNG, and BMP).
PIL also provides tools for image processing, including geometric transforms, thumbnail
creation, format conversions, and much more.
'''

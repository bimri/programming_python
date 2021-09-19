
"Performance: Saving thumbnail files"
"""
same, but make thumb images in memory without saving to or loading from files:
seems just as fast for small directories, but saving to files makes startup much
quicker for large image collections; saving may be needed in some apps (web pages)
"""

import os, sys
from PIL import Image
from tkinter import Tk
import viewer_thumbs


def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    get thumbnails for all images in a directory; for each, create and save a
    new thumb image; return a list of thumbnails
    """
    thumbs = []
    for imgfile in os.listdir(imgdir):
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath)            # make image object from file
            imgobj.thumbnail(size)
            thumbpath = os.path.join(imgdir, subdir, imgfile)
            imgobj.save(thumbpath)                  # save thumb image to new file
            thumbs.append(thumbpath)
        except:
            print("Skipping: ", imgpath)
    return thumbs


if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'images'
    maindir, subdir = os.path.split(imgdir)
    size = (200, 200)
    thumbs = makeThumbs(imgdir, size, subdir)
    viewer_thumbs.view_thumbs(thumbs, maindir, subdir, size)

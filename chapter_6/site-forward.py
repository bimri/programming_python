"""
################################################################################
Create forward-link pages for relocating a web site.
Generates one page for every existing site html file; upload the generated
files to your old web site. See ftplib later in the book for ways to run
uploads in scripts either after or during page file creation.
################################################################################
"""

import os 
servername   = 'learning-python.com'                                        # where site is relocating to
homedir      = 'books'                                                      # where site will be rooted
sitefilesdir = r'E:\practice\programming_python\chapter_6>public_html'      # where site files live locally
uploaddir    = r'E:\practice\programming_python\chapter_6>isp-forward'      # where to store forward files
tmeplatename = 'template.html'                                              # template for generated pages

try:
    os.mkdir(uploaddir)                                                     # make upload dir if needed
except OSError: pass

template  = open(tmeplatename).read()                                        # load or import template text
sitefiles = os.listdir(sitefilesdir)                                         # filenames, no directory prefix

count = 0
for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = os.path.join(uploaddir, filename)                         # forward file name
        print('Creating:', fwdname, 'as', fwdname)
        filetext = template.replace('$ServerName', servername)              # insert text
        filetext = filetext.replace('$HomeDir', homedir)                    # and write
        filetext = filetext.replace('$file', filename)                      # file varies
        open(fwdname, 'w').write(filetext)                                  # write to file
        count += 1

print('Last file =>\n', filetext, sep='')
print('Done:', count, 'forward files created.')

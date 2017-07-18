#!/usr/bin/python3
#
#A function that creates a archive with a truncated directory tree

import os, glob, zipfile, shutil

def archiver(path):
    '''Create a Zip archive, truncated to the basename of its path'''
    archive_name = os.path.abspath(os.path.basename(path) + '.zip')
    zf = zipfile.ZipFile(archive_name, 'w')
    inventory = glob.glob(os.path.join(path, '*'))
    for item in inventory:
        if os.path.isfile(item):
            base = os.path.basename(os.path.dirname(item))
            source = os.path.basename(item)
            join = os.path.join(base, source)
            try:
                zf.write(join)
            except:
                if not os.path.exists(base):
                    os.mkdir(base)
                shutil.copy(item, base)
                zf.write(join)   
                shutil.rmtree(base)


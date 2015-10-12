#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michał Pomarański
# grupa nr 3

from distutils.core import setup
import py2exe, sys, os
from globals import ikonki_directory

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')

image_directory = "E:\Dev\Minesweeper\ikonki\"
Mydata_files = []
for files in os.listdir(image_directory):
    f1 = image_directory + files
    if os.path.isfile(f1): # skip directories
        f2 = 'ikonki', [f1]
        Mydata_files.append(f2)

setup(
    icon_file="ikonki/icon_saper.ico",
    data_files = Mydata_files,
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "main.py",
    'icon_resources': [(1, os.path.join(ikonki_directory, 'icon_saper.ico'))]




    }],
    zipfile = None,
)

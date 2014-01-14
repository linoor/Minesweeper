# -*- coding: utf-8 -*-
""" Skrypt tworzący plik .exe """
import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = "WIN32GUI"

includefiles = [
    'Block.py', 'clock.py', 'colors.py', 'counter.py', 'difficulty.py', 'game.py', 'globals.py',
    'kenzo.otf',
    'ikonki/']
excludes = ['Tkinter']
packages = []

setup(
    name='Saper',
    version='1.1.0',
    description='Saper napisany w PyGame',
    author='Michal Pomaranski',
    author_email='michal.pomaranski@gmail.com',
    options={'build_exe': {'excludes': excludes,
                           'packages': packages, 'include_files': includefiles}},
    executables=[Executable('main.py', base=base)]
)

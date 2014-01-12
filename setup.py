from cx_Freeze import setup,Executable

includefiles = ['Block.py', 'clock.py', 'colors.py', 'counter.py', 'difficulty.py', 'game.py', 'globals.py',
'kenzo.otf',
'ikonki/']
excludes = ['Tkinter']
packages = []

setup(
    name = 'Saper',
    version = '1.0.0',
    description = 'Saper napisany w PyGame',
    author = 'Michal Pomaranski',
    author_email = 'michal.pomaranski@gmail.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('main.py')]
)
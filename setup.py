from distutils.core import setup
import py2exe, sys, os

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
       if os.path.basename(pathname).lower() in ["sdl_ttf.dll"]:
               return 0
       return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')
sys.argv.append('--icon icon_saper.ico')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "main.py",
    'icon_resources': [(1, os.path.join('ikonki', 'icon_saper.ico'))]




    }],
    zipfile = None,
)
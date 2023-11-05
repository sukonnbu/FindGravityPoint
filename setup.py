from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('show_graph.py', base=base, target_name = 'FIND_GRAVITY_POINT')
]

setup(name='Find Gravity Point',
      version = '1',
      description = 'Show Gravity Point of Polygons',
      options = {'build_exe': build_options},
      executables = executables)

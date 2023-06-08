# from pathlib import Path
# p = Path('.')
# [x for x in p.iterdir() if x.is_dir()]
# list(p.glob('**/*.py'))
# p = Path('/etc')
# q = p / 'init.d' / 'reboot'
# q # PosixPath('etc/init.d/'reboot')
# q.resolve() # PosixPath('etc/rc.d/init.d/halt')
# q.exists() # True
# q.is_dir() # False
# with q.open() as f: f.readline()

from pathlib import PurePath
from pathlib import Path
from pathlib import PureWindowsPath
import os

# PurePath('setup.py')
# PurePath('foo', 'some/path', 'bar')
# PurePath(Path('foo'), Path('bar'))
# PurePath()
# PurePath('etc', '/usr', 'lib64')
# PureWindowsPath('c:/Windows', 'd:bar')
# PureWindowsPath('c:/Program Files')
# PurePath('foo//bar')
# PurePath('foo/./bar')
# PurePath('foo/../bar')

# some spurious statements:
# PurePosixPath('foo') == PurePosixPath('FOO') # false
# PureWindowsPath('foo') == PureWindowsPath('FOO') # true
# PureWindowsPath('FOO') in { PureWindowsPath('foo') } # true
# PureWindowsPath('C:') < PureWindowsPath('d:') # true
#
# p = PurePath('/etc')
# p
# p / 'init.d' / 'apache2'
# q = PurePath('bin')

import os
# p = PurePath('/etc')
# os.fspath(p)
# # '/etc'

# p = PurePath('/etc')
# str(p)
# p = PureWindowsPath('c:/Program Files')
# str(p)
# bytes(p)

# p = PurePath('/usr/bin/python3')
# p.parts
#
# p = PureWindowsPath('c:/Program Files/PSF')
# p.parts()


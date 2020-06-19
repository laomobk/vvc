import os.path


_SCRIPT = '''#!{py3path}

import sys

from vvc import cmd_main


cmd_main.run_vvc_command(sys.argv[1:])
'''


print('This script will create vvc executable script in .../bin/')
b = input('please enter bin path: ')


try:
    with open(os.path.join(b, 'vvc'), 'w') as f:
        print('[A] writing script...')
        f.write(_SCRIPT.format(py3path=os.path.join(b, 'python3')))

        print('[A] make it executable...')
        os.system('chmod 777 %s' % os.path.join(b, 'vvc'))

        print('[A] successfully create vvc executable script!')
except Exception as e:
    print('[E] failed to create vvc executable script: %s' % e)

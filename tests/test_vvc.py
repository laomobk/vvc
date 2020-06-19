import sys

from vvc import cmd_main

test_env_path = 'testenv/vimrc.txt'

cmd_main.run_vvc_command(sys.argv[1:])

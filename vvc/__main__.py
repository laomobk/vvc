import sys

from .cmd_main import run_vvc_command


sys.exit(run_vvc_command(sys.argv[1:]))

from os.path import exists

from .vvc import VimrcVersionController
from .find import find_or_ask_vimrc_auto


_USAGE_STR = \
'''Usage:
    vvc [ch | new | rm | list | match | set | help] arg'''

_HELP_STR = _USAGE_STR + \
'''
    ch    [name]    -- change vimrc version
    new   [name]    -- new vimrc version record
    rm    [name]    -- remove a vimrc version record
    list  [all]     -- list all vimrc version record
    match [version] -- version now vimrc matched
    set   [path]    -- set default .vimrc path

    help  -- get help'''


def print_usage():
    print(_USAGE_STR)


def print_help():
    print(_HELP_STR)


def run_vvc_command(args :list, vimrc_path_test=None) -> int:
    try:
        action, arg = args
    except ValueError:
        if args == ['help']:
            print_help()
            return 0

        else:
            print_usage()
            return 1

    vimrc_path = vimrc_path_test
    
    if vimrc_path_test is None:
        vimrc_path = find_or_ask_vimrc_auto()

    vvc = VimrcVersionController(vimrc_path)

    if action == 'ch':
        return vvc.change_version(arg)

    elif action == 'new':
        return vvc.new_version(arg)

    elif action == 'rm':
        return vvc.remove_version(arg)

    elif action == 'list':
        return vvc.list_version()

    elif action == 'match':
        return vvc.now_vimrc_version()

    elif action == 'set':
        from .config import CONFIG
        from .find import KEY_VIMRC_PATH

        if not exists(arg):
            print('[E] .vimrc not found')
            return 1

        CONFIG[KEY_VIMRC_PATH] = arg

        print('[A] successfully set .vimrc path')

        return 0

    else:
        print_usage()
        return 1


if __name__ == '__main__':
    import sys

    run_vvc_command(sys.argv[1:])

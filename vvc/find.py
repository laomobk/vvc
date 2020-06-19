from os.path import join, exists, isdir
from os import environ

from .config import CONFIG


KEY_VIMRC_PATH = 'vimrc_path'


def find_vimrc_auto() -> str:
    cfgp = CONFIG.get(KEY_VIMRC_PATH, None)
    if cfgp is not None:
        return cfgp

    h = environ.get('HOME', None)

    if h is None:
        return None

    rcp = join(h, '.vimrc')

    if not exists(rcp):
        return None

    return rcp


def find_home(ask=False) -> str:
    h = environ.get('HOME', None)

    if h is not None:
        return h

    while ask:
        h = input('[A] Please enter HOME path: ')
        if exists(h) and isdir(h):
            return h

        print('[E] Incorrect path, try another!')


def find_or_ask_vimrc_auto() -> str:
    vp = find_vimrc_auto()

    if vp is not None:
        return vp

    vp = input('[A] please enter .vimrc path: ')

    while not exists(vp):
        vp = input('[A] .vimrc not found, please try again: ')
    
    CONFIG[KEY_VIMRC_PATH] = vp

    print('[A] .vimrc path save automatically.')

    return vp

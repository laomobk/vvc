
from os.path import dirname, join


VVC_DIR = dirname(__file__)


def relative(path :str) -> str:
    return join(VVC_DIR, path)

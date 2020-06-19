import sys
import importlib


def run_test(module):
    for k, v in module.__dict__.items():
        if k[:4] == 'test' and hasattr(v, '__call__'):
            v()


if __name__ == '__main__':
    n = sys.argv[1]
    m = importlib.import_module(n)
    run_test(m)

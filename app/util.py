"""
Some helper functions

@author Lukas Zimmermann
"""
import sys


def fatal_if(test: bool, msg: str, exit_code: int):
    if test:
        print('FATAL: {}'.format(msg), file=sys.stderr)
        sys.exit(exit_code)

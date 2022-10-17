#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
    except BaseException as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return
    return result

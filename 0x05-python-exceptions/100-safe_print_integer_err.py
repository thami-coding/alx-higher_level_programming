#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        if not isinstance(value, int):
            raise ValueError("Unknown format code 'd' " +
                             "for object of type 'str'")
        print("{:d}".format(int(value)))
        return True
    except ValueError as e:
        print("Exception:", e, file=sys.stderr)
        return False

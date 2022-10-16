#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not isinstance(value, int):
            raise Exception
    except BaseException:
        return False
    else:
        print("{:d}".format(value))
        return True

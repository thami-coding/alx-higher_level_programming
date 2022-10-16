#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = float(a/b)
    except ZeroDivisionError:
        pass
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
            return result
        else:
            print("Inside result: {}".format(None))

#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a/b
    except ZeroDivisionError:
        pass
    finally:
        if result:
            print("Inside result: {} ".format(result))
            return result
        else:
            print("Inside result: {} ".format(None))

#!/usr/bin/python

"""
This module provides a function to safely print
the first 'x' elements of a list.

Functions:
- safe_print_list(my_list=[], x=0): Print the
first 'x' elements of a list safely.
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count

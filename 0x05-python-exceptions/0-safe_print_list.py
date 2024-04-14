#!/usr/bin/python

"""
This module provides a function to safely print
the first 'x' elements of a list.

Functions:
- safe_print_list(my_list=[], x=0): Print the
first 'x' elements of a list safely.
"""


def safe_print_list(my_list=[], x=0):
    """
    Print the first 'x' elements of a list safely.

    Parameters:
    - my_list (list, optional): The input list containing
      elements of any type. Defaults to an empty list.
    - x (int, optional): The number of elements to print
    from the list. Defaults to 0.

    Returns:
    - int: The real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
        print()
    except IndexError:
        pass
    return count

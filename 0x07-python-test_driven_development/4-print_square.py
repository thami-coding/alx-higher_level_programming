#!/usr/bin/python3
"""
print_square module
This module has on function print_square(size) that prinsts a square
"""


def print_square(size=10):
    """
    size must be an integer, otherwise
    raises a TypeError exception
    if size is a float and is less than 0,
    raise a TypeError exception
    prints square using #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()

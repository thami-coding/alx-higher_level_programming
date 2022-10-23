#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer  module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")

    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)
    return a + b

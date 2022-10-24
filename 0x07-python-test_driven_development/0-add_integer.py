#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer  module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
     if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
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

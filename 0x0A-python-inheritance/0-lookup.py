#!/usr/bin/python3


"""
This module provides a function to lookup the available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Parameters:
        obj: The object whose attributes and methods
        are to be looked up.

    Returns:
        list: A list containing the names of attributes
        and methods of the object.

    """
    return dir(obj)

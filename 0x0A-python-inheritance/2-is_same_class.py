#!/usr/bin/python3
"""
This module provides a function to check if an object
is exactly an instance of the specified class. if it
is not the exact instance false is returned
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance
    of the specified class.

    Parameters:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance
        of a_class, False otherwise.
    """
    return type(obj) == a_class

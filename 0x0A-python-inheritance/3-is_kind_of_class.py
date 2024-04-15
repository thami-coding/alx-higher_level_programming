#!/usr/bin/python3
"""
This module provides a function to check if an object
is an instance of, or if the object is an instance of a
class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the
    object is an instance of a class that inherited from,
    the specified class.

    Parameters:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class
        or a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class)

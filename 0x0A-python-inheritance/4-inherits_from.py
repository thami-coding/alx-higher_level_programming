#!/usr/bin/python3

"""
This module provides a function to check if an object
is an instance of a class that inherited (directly or indirectly)
of the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited (directly or indirectly) of the specified class.

    Parameters:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a
        subclass of a_class (directly or indirectly),
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

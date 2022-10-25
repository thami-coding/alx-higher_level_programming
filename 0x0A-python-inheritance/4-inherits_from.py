#!/usr/bin/python3
"""
inherits_from module
has one function inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is
    an instance of a class that
    inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if type(obj) == a_class:
        return False
    if isinstance(obj, a_class):
        return True
    return False

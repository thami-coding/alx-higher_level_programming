#!/usr/bin/python3

"""Module has one class BaseGeometry"""


class BaseGeometry:
    """
    Represents a base geometry class.

    Methods:
        area(self): Raises an Exception with
        the message 'area() is not implemented'.
    """

    def area(self):
        """
        Raises an Exception indicating that
        the method is not implemented.
        """
        raise Exception("area() is not implemented")

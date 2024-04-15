#!/usr/bin/python3


"""
This module defines a class MyList that inherits
the built-in list class.
"""


class MyList(list):
    """
    Represents a custom list class inheriting
    the built-in list class.

    Attributes:
        Inherits all attributes and methods
        the built-in list class.

    Methods:
        print_sorted(self): Prints the list
        sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

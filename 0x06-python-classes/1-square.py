#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new
        Square instance with the given size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size

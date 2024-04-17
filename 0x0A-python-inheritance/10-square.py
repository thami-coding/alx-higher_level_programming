#!/usr/bin/python3

"""Module has two classes BaseGeometry and Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square
        object with the given size.
        area(self): Computes and returns the area of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

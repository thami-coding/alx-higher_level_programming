#!/usr/bin/python3

"""Module has two class BaseGeometry and Rectangle"""


class BaseGeometry:
    """
    Represents a base geometry class.

    Methods:
        area(self): Raises an Exception with the
        message 'area() is not implemented'.
        integer_validator(self, name, value): Validates
        the given value as an integer.
    """

    def area(self):
        """
        Raises an Exception indicating that the
        method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle object with the given width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

#!/usr/bin/python3

"""Module has one class BaseGeometry"""


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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

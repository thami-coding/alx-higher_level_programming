#!/usr/bin/python3

"""
Module has three classes BaseGeometry and Rectangle
 and Square
 """


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
        __init__(self, width, height): Initializes
        new Rectangle object with the given width and height.
        area(self): Computes and returns the area of the
        rectangle.
        __str__(self): Returns the string representation of
        the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with
        the given width and height.

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

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Represents a square inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new
        Square object with the given size.
        area(self): Computes and returns the area
        of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square object with
        the given size.

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

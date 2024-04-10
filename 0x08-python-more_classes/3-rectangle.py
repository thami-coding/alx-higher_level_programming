#!/usr/bin/python3
"""module contains one Rectangle class based on 0-rectangle.py"""


class Rectangle:
    """Rectangel class calculates area and perimeter of rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Area of a triangle"""
        return self.width * self.height

    def perimeter(self):
        return (
            0
            if self.width == 0 or self.height == 0
            else self.width * 2 + self.height * 2
        )

    def __str__(self):
        string = ""

        if self.width == 0 or self.height == 0:
            return string

        for _, index in enumerate(range(self.height)):
            for _ in range(self.width):
                string += "#"
            if not (index == self.height - 1):
                string += "\n"
        return string

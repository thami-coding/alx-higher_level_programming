#!/usr/bin/python3
"""Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def integer_validator(self, name, value):
        super().integer_validator(name, value)
        return value

    def __str__(self):
        return "[Rectangle] {}/{}"\
                .format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

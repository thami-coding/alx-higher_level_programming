#!/usr/bin/python3
"""Square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        self.__width = super().integer_validator("width", size)
        self.__height = super().integer_validator("height", size)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

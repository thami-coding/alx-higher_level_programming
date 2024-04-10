#!/usr/bin/python3
"""module contains one Rectangle class based on 0-rectangle.py"""


class Rectangle:
    """Rectangel class calculates area and perimeter of rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                string += str(self.print_symbol)
            if not (index == self.height - 1):
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            TypeError("rect_1 must be an instance of Rectangle")

        if not (isinstance(rect_1, Rectangle)):
            TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            rect_2
        else:
            rect_1
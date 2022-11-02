#!/usr/bin/python3
"""
This module has one class Rectangle
that inherits from the Base class
"""


from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        keys = ['id', 'x', 'y', 'width', 'height']
        values = []
        for key in keys:
            values.append(getattr(self, key))
        return "[Rectangle] ({}) {}/{} - {}/{}"\
.format(*values)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height  must be an integer")
        elif value <= 0:
            raise ValueError("height  must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        for i in range(y):
            print()
        for row in range(height):
            for col in range(width):
                if col == 0:
                    for i in range(x):
                        print(" ", end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        keys = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i > len(args) - 1:
                    break
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        keys = ['id', 'width', 'height', 'x', 'y']
        obj_dict = {}
        for key in keys:
            obj_dict[key] = getattr(self, key)
        return obj_dict

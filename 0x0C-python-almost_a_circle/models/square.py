#!/usr/bin/python3
"""
This module has one class Square
that inherits from Rectangle
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class creates a square instance
    with size, x, y dimensions.inherits
    most of its fields from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        keys = ['id', 'x', 'y', 'size']
        values = []
        for key in keys:
            values.append(getattr(self, key))

        return "[Square] ({}) {}/{} - {}".format(*values)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update a square instance base on the values of
        args or kwargs. if args exists skip kwargs
        else use kwargs
        """

        keys = ['id', 'size', 'x', 'y']
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                if i > len(keys) - 1 or i == len(args):
                    break
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        convert a square instance into a dictionary using
        its fields
        """

        keys = ['id', 'x', 'size', 'y']
        obj_dict = {}
        for key in keys:
            obj_dict[key] = getattr(self, key)
        return obj_dict

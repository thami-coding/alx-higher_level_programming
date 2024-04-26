#!/usr/bin/python3
"""Module containing the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square.

    This class inherits from the Rectangle class and
    represents a square
    with equal width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the top-left
            corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
            corner of the square. Defaults to 0.
            id (int, optional): The ID to assign to the square.
            Defaults to None.

        Raises:
            TypeError: If size, x, y, or id is not an integer.
            ValueError: If size, x, or y is less than 0.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: The positional arguments to assign to each attribute.
            **kwargs: The keyword arguments to assign to attributes.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

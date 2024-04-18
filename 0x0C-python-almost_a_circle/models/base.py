#!/usr/bin/python3

"""Module containing the Base class for managing IDs."""


class Base:
    """Base class for managing IDs.

    This class manages the ID attribute for
    all other classes in the project.
    It ensures that each instance has a
    unique ID assigned.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID.

        Args:
            id (int, optional): The ID to assign to the instance.
            If None, a unique ID will be generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

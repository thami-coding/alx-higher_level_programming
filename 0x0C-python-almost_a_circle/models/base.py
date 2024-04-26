#!/usr/bin/python3

"""Module containing the Base class for managing IDs."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of
        list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting
            from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented
        by json_string.

        Args:
            json_string (str): A string representing a list
            of dictionaries in JSON format.

        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from
        the dictionary.

        Args:
            **dictionary: Keyword arguments representing
            attribute values.

        Returns:
            Base: An instance of the class with attributes set from
            the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError("Class not supported")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in dictionaries]
        except FileNotFoundError:
            return []

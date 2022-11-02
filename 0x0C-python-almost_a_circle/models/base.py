#!/usr/bin/python3
"""
base model has one class called
Base class with a private class attribute __nb_objects = 0
"""


import json
from os.path import exists


class Base:
    """
    This class will be the “base” of
    all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a json string reprenstation
        of list of dictionaries
        """

        if list_dictionaries is not None:
            if len(list_dictionaries) != 0:
                return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a list object as a dictionary
        in json string format to a file
        """

        obj_list = []
        keys = ['id', 'width', 'height', 'size', 'x', 'y']

        if list_objs is not None and len(list_objs) != 0:
            for obj in list_objs:
                obj_dict = {}
                for key in keys:
                    if hasattr(obj, key):
                        obj_dict[key] = getattr(obj, key)

                obj_list.append(obj_dict)

        serialized = cls.to_json_string(obj_list)
        filename = cls.__name__ + ".json"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(serialized)

    @staticmethod
    def from_json_string(json_string):
        """
        deserializes a json string
        """
        if json_string is not None:
            if len(json_string) != 0:
                return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        creates a dummy Rectangle or Square instances
        based on cls and then updates the values
        of this dummy instance
        """

        dummy = cls(10, 10, 10, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not (exists(filename)):
            return []

        with open(filename, 'r+', encoding='utf-8') as f:
            serialized_list = f.read()
            obj_list = cls.from_json_string(serialized_list)
            new_objs = []
            for obj in obj_list:
                new_obj = cls.create(**obj)
                new_objs.append(new_obj)
        return new_objs

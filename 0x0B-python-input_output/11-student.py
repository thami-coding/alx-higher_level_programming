#!/usr/bin/python3
"""
This module has one class
Student that defines a student by first_name,
last_name, age
"""


class Student:
    """
    class Student defines a student by first_name,
    last_name, age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj_dict = self.__dict__
        new_dict = {}
        if isinstance(attrs, list):
            if len(attrs) >= 1:
                for key in list(obj_dict.keys()):
                    if key in attrs:
                        new_dict[key] = obj_dict[key]
            else:
                return {}
        obj_dictionary = new_dict or obj_dict

        for key, value in list(obj_dictionary.items()):
            if not (type(value) == int or
                    type(value) == float or
                    type(value) == str or
                    type(value) == list or
                    type(value) == dict or
                    type(value) == bool):
                del obj_dictionary[key]
            return obj_dictionary

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

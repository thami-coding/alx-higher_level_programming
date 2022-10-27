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

    def to_json(self):
        obj_dict = self.__dict__
        print(obj_dict)
        for key, value in list(obj_dict.items()):
            if not (type(value) == int or
                    type(value) == float or
                    type(value) == str or
                    type(value) == list or
                    type(value) == dict or
                    type(value) == bool):
                del obj_dict[key]
            return obj_dict

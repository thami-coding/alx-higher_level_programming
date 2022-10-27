#!/usr/bin/python3
"""
This module has one function class_to_json(obj)
that returns All attributes of the obj Class
that are serializable
"""


def class_to_json(obj):
    """
    returns the dictionary description
    with simple data structure (list,
    dictionary, string, integer and
    boolean) for JSON serialization of
    an object
    """

    obj_dict = obj.__dict__
    for key, value in list(obj_dict.items()):
        if not (type(value) == int or
                type(value) == float or
                type(value) == str or
                type(value) == list or
                type(value) == dict or
                type(value) == bool):
            del obj_dict[key]
    return obj_dict

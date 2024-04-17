#!/usr/bin/python3
"""
This module provides a function to return the
dictionary description with simple data structure
for JSON serialization of an object.

Functions:
    class_to_json(obj): Returns the dictionary description
    with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure for JSON serialization of an object.

    Args:
        obj: An instance of a Class with all attributes being
        serializable: list, dictionary, string, integer, and boolean.

    Returns:
        dict: The dictionary description with simple data structure for
        JSON serialization of the object.
    """
    json_dict = {}
    for attr in obj.__dict__:
        if isinstance(getattr(obj, attr), (list, dict, str, int, bool)):
            json_dict[attr] = getattr(obj, attr)
    return json_dict

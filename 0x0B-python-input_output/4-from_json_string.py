#!/usr/bin/python3
"""
This module provides a function to return
an object (Python data structure) represented by a JSON string.

Functions:
    from_json_string(my_str): Returns an object
    (Python data structure) represented by a JSON string.

"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented
    by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a
        Python object.

    Returns:
        object: The Python object represented by the JSON string,
        or None if the string is not valid JSON.
    """
    import json
    return json.loads(my_str)

"""
This module provides a function to return the
JSON representation of an object (string).

Functions:
    to_json_string(my_obj): Returns the JSON
    representation of an object (string).
"""
def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object, or an empty string if the object can't be serialized.
    """
    import json
    return json.dumps(my_obj)

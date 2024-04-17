#!/usr/bin/python3
"""
This module provides a function to create
an object from a JSON file.

Functions:
    load_from_json_file(filename): Creates an
    object from a JSON file.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the
        JSONfile from which the object will be created.

    Returns:
        object: The object created from the JSON file,or
        None if the file doesn't contain valid JSON.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

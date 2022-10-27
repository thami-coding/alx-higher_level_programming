#!/usr/bin/python3
"""
This module has one function from_json_string(my_str)
that returns a python data structure from serialization
"""


import json


def from_json_string(my_str):
    """
    eturns an object (Python data structure)
    represented by a JSON string
    """

    return json.loads(my_str)

#!/usr/bin/python3
import json
"""
This module has one function to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """
    eturns the JSON representation
    of an object (string)
    """
    return json.dumps(my_obj)

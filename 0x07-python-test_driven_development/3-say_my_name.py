#!/usr/bin/python3
"""
This is the prints  module.
it has one function, prints(first_name, last_name)
"""


def say_my_name(first_name, last_name=""):
    """
    first_name and last_name must
    be strings otherwise, raises a
    TypeError exception

    prints My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "" or last_name == "":
        print()
    else:
        print("My name is {} {}".format(first_name, last_name))

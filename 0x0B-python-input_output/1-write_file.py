#!/usr/bin/python3
"""
write_file module. This module has one function
write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    and returns the number of characters
    written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

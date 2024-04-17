#!/usr/bin/python3
"""
This module provides a function to write a
string to a text file (UTF-8) and return the
number of characters written.

Functions:
    write_file(filename="", text=""): Writes a
    string to a text file (UTF-8) and returns the
    number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.

    Args:
        filename (str, optional): The path to
        the file to write to. Defaults to "".
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written

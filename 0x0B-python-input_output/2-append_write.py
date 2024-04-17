"""
This module provides a function to append a
string to the end of a text file (UTF-8) and
return the number of characters added.

Functions:
    append_write(filename="", text=""): Appends a
    string to the end of a text file (UTF-8) and returns
    the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    (UTF-8) and returns the number of characters added.

    Args:
        filename (str, optional): The path to the file to
        append to. Defaults to "".
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added

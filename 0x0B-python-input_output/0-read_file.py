#!/usr/bin/python3
"""
This module provides a function to read a text file
and print its contents to stdout.

Functions:
    read_file(filename=""): Reads a text file and prints
    its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str, optional): The path to the file to
        be read. Defaults to "".

    Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If an error occurs during file reading.

    Returns:
        None
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("not found.")
    except Exception as e:
        print("An error occurred:", e)

#!/usr/bin/python3
"""
read_file module, this module has one function,
read_file(filename="")
"""


def read_file(filename=""):
    """
    reads a file and
    prints to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

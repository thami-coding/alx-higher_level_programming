#!/usr/bin/python3
"""
text_indentation module
This module has on function text_indentation(text)
"""


def text_indentation(text):
    """
    prints a text with 2
    new lines after each of
    these characters: ., ? and :

    text must be a string,
    otherwise raise a TypeError exception
    """
    matches = [".", "?", ":"]
    i = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if i in matches:
            i = ""
            continue
        print(char, end="")
        for match in matches:
            if match == char:
                i = char
                print()
                print()

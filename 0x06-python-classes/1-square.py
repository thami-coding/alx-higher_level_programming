#!/usr/bin/python3
"""Square module"""


class Square:
    """square class that initializes a square"""
    def __init__(self, size):
        self.__size = size

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

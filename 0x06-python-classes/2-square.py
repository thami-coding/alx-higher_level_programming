#!/usr/bin/python3
""" Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        self.set_size(size)

    def set_size(self, s):
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s

    def get_size(self):
        return self.__size

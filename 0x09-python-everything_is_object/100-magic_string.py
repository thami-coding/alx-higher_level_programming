#!/usr/bin/python3
def magic_string():
    magic_string.x = getattr(magic_string,'x', 0) + 1
    return magic_string.x * "{}".format("BestSchool ")

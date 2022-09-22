#!/usr/bin/python3
def islower(character):
    for i in range(97, 123):
        if ord(character) == i:
            return True
    return False

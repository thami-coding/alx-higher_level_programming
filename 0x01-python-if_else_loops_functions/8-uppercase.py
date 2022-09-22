#!/usr/bin/python3
def uppercase(str):
    for character in str:
        num = ord(character)
        if num >= 97 and num <= 122:
            num = num - 32
        print("{}".format(chr(num)), end="")
    print()


#!/usr/bin/python3
print_square = __import__('4-print_square').print_square


print_square()
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

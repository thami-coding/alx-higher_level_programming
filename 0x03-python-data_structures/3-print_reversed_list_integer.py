#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    stop = len(my_list) + 1
    for i in range(1, stop):
        print("{:d}".format(my_list[-i]))

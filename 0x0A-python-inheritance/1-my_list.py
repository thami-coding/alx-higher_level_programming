#!/usr/bin/python3
"""
my_list module.
MyList inherits from list and has one method of its own
"""


class MyList(list):

    def print_sorted(self):
        """
        print list in ascending order
        """
        new_list = list(self)
        new_list.sort()
        print(new_list)

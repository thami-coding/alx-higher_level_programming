#!/usr/bin/python3
"""
my_list module.
MyList inherits from list and has one method
called print_sorted
"""


class MyList(list):

    def print_sorted(self):
        """
        print list in ascending order wihtout
        changing the original list
        """
        new_list = list(self)
        new_list.sort()
        print(new_list)

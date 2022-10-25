#!/usr/bin/python3
"""
my_list module.
MyList inherits from list and has one method
called print_sorted
"""


class MyList(list):

    """ This is the MYList class
    which inherits from the list
    class and has one method
    print_sorted
    """
    def __str__(self):
        return "sorts a list"
    def print_sorted(self):
        """
        print list in ascending order wihtout
        changing the original list
        """
        print(sorted(self))
        return sorted(self)

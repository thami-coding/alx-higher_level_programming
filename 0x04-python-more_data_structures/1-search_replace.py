#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for item in my_list:
        return [x if x is not search else replace for x in my_list]

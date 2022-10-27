#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
and then save them to a file
"""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
new_list = sys.argv[1:]
file_exists = exists(filename)

if file_exists:
    list_from_file = load_from_json_file(filename)
    list_from_file += new_list
    save_to_json_file(list_from_file, filename)
else:
    save_to_json_file(new_list, filename)

#!/usr/bin/python3
"""
This script adds all arguments to a Python list
and then saves them to a file using JSON representation.

The script utilizes functions from other modules:
- save_to_json_file: to save the list as a JSON
representation in a file.
- load_from_json_file: to load the list from the JSON file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_items_to_list():
    try:
        items = load_from_json_file("add_item.json")
    except Exception:
        items = []

    # Add new items from command line arguments
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    add_items_to_list()

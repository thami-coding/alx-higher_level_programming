#!/usr/bin/python3
def best_score(a_dictionary):
    key_max = ''
    max_value = 0
    if not a_dictionary:
        return
    for key, value in a_dictionary.items():
        if value > max_value:
            key_max = key
            max_value = value
    return key_max

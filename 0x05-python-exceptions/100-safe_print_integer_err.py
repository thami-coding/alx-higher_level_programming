#!/usr/bin/python3
def safe_print_integer_err(value):
    if isinstance(value, int):
        raise TypeError

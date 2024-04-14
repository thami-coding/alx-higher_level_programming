#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print the first 'x' elements of a list safely.

    Parameters:
    - my_list (list, optional): The input list containing
      elements of any type. Defaults to an empty list.
    - x (int, optional): The number of elements to print
    from the list. Defaults to 0.

    Returns:
    - int: The real number of elements printed.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

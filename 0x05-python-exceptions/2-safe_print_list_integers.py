#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first 'x' integers from a list.

    Parameters:
    - my_list (list, optional): The input list containing
    elements of any type. Defaults to an empty list.
    - x (int, optional): The number of elements to access
    from the list. Defaults to 0.

    Returns:
    - int: The real number of integers printed.
    """
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                count += 1
    except IndexError:
        raise
    finally:
        print()
    return count

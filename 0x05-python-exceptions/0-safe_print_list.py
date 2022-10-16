#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0:
        return 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except BaseException:
            i -= 1
            break
    print()
    return i + 1

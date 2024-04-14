#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                num1 = float(my_list_1[i]) if isinstance(
                    my_list_1[i], (int, float)) else None
                num2 = float(my_list_2[i]) if isinstance(
                    my_list_2[i], (int, float)) else None

                if num1 is None or num2 is None:
                    print("wrong type")
                    result_list.append(0)
                elif num2 == 0:
                    print("division by 0")
                    result_list.append(0)
                else:
                    result_list.append(num1 / num2)
            except IndexError:
                print("out of range")
                result_list.append(0)
    finally:
        return result_list

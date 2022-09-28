#!/usr/bin/python3
def weight_average(my_list=[]):
    my_list = dict(my_list)
    total = 0
    total2 = 0

    for k, v in my_list.items():
        total += k * v
        total2 += v
        return (total / total2)

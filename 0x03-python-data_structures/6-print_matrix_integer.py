#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print("")
        return
    for i in matrix:
        for j in range(0, len(i)):
            if j == len(i) - 1:
                print("{:d}".format(i[j]))
            else:
                print("{:d}".format(i[j]), end=" ")

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for flat in matrix:
        new_matrix.append([x * x for x in flat])
    return new_matrix

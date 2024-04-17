"""
Module: pascal_triangle_generator

This module contains a function for generating
Pascal's triangle up to a specified number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified
    number of rows.

    Parameters:
    - n (int): The number of rows in Pascal's triangle.

    Returns:
    - List[List[int]]: A list of lists of integers
    representing Pascal's triangle.
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)

        triangle.append(row)

    return triangle

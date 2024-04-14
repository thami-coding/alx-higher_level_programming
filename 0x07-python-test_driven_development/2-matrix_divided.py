#!/usr/bin/python3
"""
Module: matrix_operations

This module provides a function for dividing all elements
of a matrix by a scalar value.

Function:
- matrix_divided(matrix, div): Divides all elements of
  a matrix by a scalar value.
  Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.
  Returns:
    - list of lists: A new matrix with all elements divided
       by the divisor, rounded to 2 decimal places.
  Raises:
    - TypeError: If matrix is not a list of lists of
                integers or floats,
                or if each row of the matrix does not have the same size,
                or if div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a scalar value.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - list of lists: A new matrix with all elements divided
      by the divisor, rounded to 2 decimal places.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats,
                or if each row of the matrix does not have the same size,
                or if div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """

    if not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(val, (int, float))
                for row in matrix for val in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    result_matrix = []
    for row in matrix:
        divided_row = [round(val / div, 2) for val in row]
        result_matrix.append(divided_row)

    return result_matrix

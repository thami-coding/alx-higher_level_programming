"""
This is the divide a matrix module.
it has one function, matrix(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    matrix must be a list of lists of
    integers or floats
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")

    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div != div:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    result = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        row_len = len(matrix[0])
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must\
have the same size")

        for num in i:
            if isinstance(num, int) or isinstance(num, float):
                if num != num:
                    raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
                result.append(round(num/div, 2))
            else:
                raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
        new_matrix.append(result)
        result = []
    return new_matrix

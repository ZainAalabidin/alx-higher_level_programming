#!/usr/bin/python3
"""Define a function that divides all elements of matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all element of a matrix.

    Args:
        matrix (list): A list of lists of integer or floats.
        div (int/float): A number that divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix isn't of the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        matrix: result of division.
    """
    row_size = None
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        for colm in row:
            if not isinstance(colm, int) and not isinstance(colm, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

        if row_size is None:
            row_size = len(row)

        elif row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    new_matrix = [[round(colm / div, 2) for colm in row] for row in matrix]

    return new_matrix

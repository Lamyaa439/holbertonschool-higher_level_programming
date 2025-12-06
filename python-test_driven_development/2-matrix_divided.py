#!/usr/bin/python3
"""
Module 2-matrix_divided
Defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with the result of the division.
    """
    # Error messages
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    div_err = "div must be a number"
    zero_err = "division by zero"

    # 1. Validate matrix structure (Type and Content)
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_err)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_err)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(type_err)

    # 2. Validate row sizes
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(size_err)

    # 3. Validate div (Type and Value)
    if not isinstance(div, (int, float)):
        raise TypeError(div_err)

    if div == 0:
        raise ZeroDivisionError(zero_err)

    # 4. Perform division and create new matrix
    new_matrix = []
    for row in matrix:
        new_row = [round(x / div, 2) for x in row]
        new_matrix.append(new_row)

    return new_matrix

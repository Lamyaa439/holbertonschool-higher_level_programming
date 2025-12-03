#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = 0
    for row in matrix:
        new_row = []
        for coulm in row:
            new_row.append(coulm**2)
        new_matrix.append(new_row)
    return new_matrix

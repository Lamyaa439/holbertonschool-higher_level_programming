#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    square = 0
    for row in matrix:
        for coulm in row:
            square = matrix[row][coulm]
            square **= 2
            new_matrix[row][matrix] += square
    return new_matrix

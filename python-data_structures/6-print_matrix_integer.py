#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cloum in row:
            print("{:d}".format(cloum), end=" ")
        print('\n')

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                separator = ""
            else:
                separator = " "
            print("{}".format(row[i]), end = separator)
        print()

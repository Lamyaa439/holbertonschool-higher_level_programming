#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        value *= 2
        print("{}: {}".format(key, value))

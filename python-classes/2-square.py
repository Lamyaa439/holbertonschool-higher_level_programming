#!/usr/bin/python3
"""
0-square.py moduls to create a class
"""


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size = 0):
        """
        method to define Private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

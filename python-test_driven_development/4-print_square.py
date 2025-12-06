#!/usr/bin/python3
"""
Module 4-print_square
Defines a function that prints a square.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    # 1. Check if size is an integer
    # Note: We do this first to catch negative floats as TypeErrors
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # 2. Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # 3. Print the square
    for i in range(size):
        print("#" * size)

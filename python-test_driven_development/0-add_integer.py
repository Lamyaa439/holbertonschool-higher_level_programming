#!/usr/bin/python3
"""
Module 0-add_integer
Defines a function that adds integers.
"""
def add_integer(a, b=98):
    """
    Returns the addition of a and b.

    Args:
        a: The first value, must be an int or float.
        b: The second value, must be an int or float. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        The integer result of the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""
This module defines a BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        a Method that raises an Exception with the message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

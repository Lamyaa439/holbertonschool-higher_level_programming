#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a base class for geometry objects.
"""


class BaseGeometry:
    """
    A class used to represent base geometry.
    """
    def area(self):
        """
        Public instance method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the 'value' parameter as a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

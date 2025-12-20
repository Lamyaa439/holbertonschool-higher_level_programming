#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from
BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        to calculate the area of the Rectangle
        """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        rectangle description: [Rectangle] <width>/<height>
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return "[Rectangle] {}/{}".format(self.__width, self.__height)

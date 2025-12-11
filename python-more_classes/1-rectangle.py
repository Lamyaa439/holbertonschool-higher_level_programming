#!/usr/bin/python3
"""
0-rectangle.py Module to create class
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle
        """
        return (self.__width)

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

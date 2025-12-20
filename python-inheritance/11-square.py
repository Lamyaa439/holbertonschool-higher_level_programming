#!/usr/bin/python3
"""
This module defines a class Square that inherits from
Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from Rectangle (9-rectangle.py)
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        method to returns the current square area
        """
        return self.__size ** 2

    def __str__(self):
        """
        square description: [Square] <width>/<height>
        """
        if self.__size == 0:
            return ""
        else:
            return "[Square] {}/{}".format(self.__size, self.__size)

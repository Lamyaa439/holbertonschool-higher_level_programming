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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        to calculate the area of the Rectangle
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """
        to calculate the perimeter of the Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            sum1 = self.__width + self.__height
            perimeter = 2 * sum1
        return perimeter

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                rect.append("#" * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

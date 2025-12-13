#!/usr/bin/python3
"""
0-rectangle.py Module to create class
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle
        """
        Rectangle.number_of_instances += 1
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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """
        print the rectangle with the character #
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print the message Bye rectangle... (... being 3 dots not ellipsis) when
        an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        del self
        print("Bye rectangle...")

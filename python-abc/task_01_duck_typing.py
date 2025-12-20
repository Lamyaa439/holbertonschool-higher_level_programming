#!/usr/bin/env python3
"""
This is model for Shapes, Interfaces, and Duck Typing
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    This is a Shape class
    """

    @abstractmethod
    def area(self):
        """
        to calclate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        to calclate perimeter
        """
        pass


class Circle(Shape):
    """
    This is a Circle class that inherits from Shape
    """

    def __init__(self, radius):
        """
        The constructor (__init__) should accept a radius.
        """
        self.radius = radius

    def area(self):
        """
        calclate the area of Circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        claclate perimeter for Circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    This is a Rectangle class, also inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        calclate the area of Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        claclate perimeter for Rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    a function named shape_info that takes a single argument.
    Print the area and perimeter of the shape passed to the function.
    """

    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

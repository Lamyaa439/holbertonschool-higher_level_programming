#!/usr/bin/env python3
"""
This module demonstrates Abstract Base Classes and Duck Typing in Python
without using the math module.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Base Class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    """

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.141592653589793

    def area(self):
        """Returns the area using A = pi * r^2"""
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter using P = 2 * pi * r"""
        return 2 * self.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area using A = w * h"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter using P = 2 * (w + h)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using Duck Typing.
    
    Args:
        shape: An object that is expected to have area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

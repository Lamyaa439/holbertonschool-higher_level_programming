#!/usr/bin/python3
"""
Module 0-square
Defines a class Square
"""


class Square:
    """
    Class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square
        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets the position of the square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i<0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # in stdout
        """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

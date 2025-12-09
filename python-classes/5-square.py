#!/usr/bin/python3
"""
0-square.py moduls to create a class
"""


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size=0):
        """
        init method
        """
        self.size = size

    @property
    def size(self):
        """
        method to getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method to setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        method to returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")

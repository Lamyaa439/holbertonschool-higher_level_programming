#!/usr/bin/python3
"""
0-square.py moduls to create a class
"""


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init method
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        method to to retrieve position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        method to to set position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i<0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


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
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            spaces = " " * self.position[0]
            print("{}".format(spaces), end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """Class with private size"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """ return square area
        Args:
        self : self
        """
        return self.__size ** 2

    @property
    def size(self):
        """ return private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ initialize the class
        Args:
        size (int): size of the square
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size__ = value

    def my_print(self):
        """prints in stdout the square with the character #
        Args:
        self : self
        """
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)

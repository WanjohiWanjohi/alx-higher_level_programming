#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """Class with private size"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """retrieves the position variable
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position
        """
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        for i in range(self.position[1]):
            print("")
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

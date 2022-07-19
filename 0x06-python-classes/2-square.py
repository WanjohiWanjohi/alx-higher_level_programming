#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """Class with private size"""

    def __init__(self, size=0):
        """ initialize the class
        Args:
           size (int): size of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

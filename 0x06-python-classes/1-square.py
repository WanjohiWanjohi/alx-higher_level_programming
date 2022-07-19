#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """Class with private size"""
    def __init__(self, size):
        """ initialize the class
        Args:
           size (int): size of the square
        """
        self.__size = size

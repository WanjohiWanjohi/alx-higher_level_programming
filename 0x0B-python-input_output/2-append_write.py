#!/usr/bin/python3

""" Appends a string to the end of a text file"""


def append_write(filename="", text=""):
    """ Appends text to file
     Args:
        filename (str): The name of the file to write.
        text (str): The text to append to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

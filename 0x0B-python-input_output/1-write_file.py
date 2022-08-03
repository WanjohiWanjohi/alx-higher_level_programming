#!/usr/bin/python3

"""  Write a string to a text file """


def write_file(filename="", text=""):
    """ Write given text to a file
     Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

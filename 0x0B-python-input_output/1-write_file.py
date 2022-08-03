#!/usr/bin/python3
"""  Write a string to a text file """


def write_file(filename="", 'w', text=""):
    with open(filename, encoding="utf-8") as f:
        return f.write(text)

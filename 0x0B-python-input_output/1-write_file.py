#!/usr/bin/python3
"""
This mudule is used to write text to a file and return the
number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    returns the number of characters written."""
    with open(filename, mode='w', encoding="utf-8") as file:
        return file.write(text)

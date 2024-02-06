#!/usr/bin/python3
"""
In this module we are declaring a function that reads from
a text file and returns the texts to the standard output
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

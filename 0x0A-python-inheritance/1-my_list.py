#!/usr/bin/python3
"""
This module shows a class MyList tha inherit from
the well known list class
so it will inherit all the public methods and attributes such as append
It also inherits the sort methos
"""


class MyList(list):
    """Inherits from list and adds a method to
    print the list in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

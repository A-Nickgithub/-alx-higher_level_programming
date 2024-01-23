#!/usr/bin/python3
"""
this is a module that will show us how to
declare and use the getter and accesser methods
"""


class Square:
    """
    This is a blueprint of a square
    Attribute:
    __size(int): to show the size of a square
    """

    def __init__(self, size=0):
        self.__size = size

        @property
        def size(self):

            return self.__size

        @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        will be used to calculate the area of a
        square by using the power of two
        """
    return self.__size ** 2

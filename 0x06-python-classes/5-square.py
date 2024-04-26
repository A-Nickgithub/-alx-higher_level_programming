#!/usr/bin/python3
"""
In this module, we define a Square class with private attributes and methods
"""


class Square:
    """
    Square class representation

    Attributes:
    __size (int): Size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print()
        else:

            for _ in range(self.__size):
                print("#" * self.__size)

#!/usr/bin/python3
"""
In this module, we define a Square class with private attributes and methods
"""


class Square:
    """
    Square class representation

    Attributes:
    __size (int): Size of the square
    __position (tuple): Position of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.
        Args:
        size (int): The size of the square. Defaults to 0.
        position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
        TypeError: If size is not an integer or
        if position is not a tuple of 2 positive integers.
        ValueError: If size is less than 0 or
        if position values are not positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
                for _ in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)

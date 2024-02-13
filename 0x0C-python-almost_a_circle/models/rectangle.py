#!/usr/bin/python3
"""Rectangle module."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance."""
        super().__init__(id)

        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """
        display rectangle in the form of #
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def area(self):
        """
        calculate and return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return string representation of the Rectangle object.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """Get width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width attribute."""
        self.__width = value

    @property
    def height(self):
        """Get height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute."""
        self.__height = value

    @property
    def x(self):
        """Get x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x attribute."""
        self.__x = value

    @property
    def y(self):
        """Get y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y attribute."""
        self.__y = value

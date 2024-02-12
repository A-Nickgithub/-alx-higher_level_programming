#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle inherited from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor for a rectangle class
        """

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

        self.__width = width
        self.__height = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        get the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of the rectangle width

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        get the value of the height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of the height

        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def y(self):
        """
        get the value of y

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set the value of y

        """
        if type(value) != int:
            raise TypeError("y must be an integr")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    @property
    def x(self):
        """
        get the value of x

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set the value of x

        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    def area(self):
        """
        calculate and return the area of the rectangle

        """

        return (self.width) * (self.height)

    def display(self):
        """
        display rectangle in the form of #

        """

        if self.width == 0 or self.height == 0:
            print("")
            return [print("") for y in range(self.y)]

        for i in range(self.height):
            [print("", end="") for x in range(self.x)]
            [print("#", end="")for j in range(self.width)]
            print()

    def __str__(self):
        """
        overiding str method from base

        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                    self.id, self.x, self.y, self.width, self.height
                    )

    @staticmethod
    def generate_setter(name, value):

        """
        return the setter in literal

        """

        setter = 'self.{} = {}'.format(name, value)

        return setter

    def update(self, *args, **kwargs):
        """
        update the object with keyword-arguments

        """

        attributes = ['id', 'width', 'height', 'x', 'y']
        for idx, x in enumerate(args):
            if idx >= len(attributes):
                return
            self.__setattr__(attributes[idx], x)
            if args:
                return

            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """
        return the dictionary representation of a rectangle

        """
        return {'id': self.id, 'width': self.width, 'height':
                self.height, 'x': self.x, 'y': self.y}

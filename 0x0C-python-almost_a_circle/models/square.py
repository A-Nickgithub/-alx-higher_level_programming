#!/usr/bin/python3
"""
This module contains the class square that inherits from
the class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square inheriting from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructure
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation of the square
        """
        return '[Square] ({}) {}/{} - {}'.format(
                    self.id, self.x, self.y, self.size
                    )

    @property
    def size(self):
        """
        get the value of the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set the value of the size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the square with keyword arguments
        """
        attributes = ['id', 'size', 'x', 'y']

        for idx, x in enumerate(args):
            if idx >= len(attributes):

                return self.__setattr__(attributes[idx], x)

            if args:
                return

            for k, v in kwargs.items():
                self.__setattr__(k, v)

    def to_dictionary(self):
        """
        dictionary representation of a square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

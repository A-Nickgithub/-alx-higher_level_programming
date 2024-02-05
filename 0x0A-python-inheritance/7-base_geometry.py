#!/usr/bin/python3

class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value and raises exceptions if not valid."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

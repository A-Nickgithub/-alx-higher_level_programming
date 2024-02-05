#!/usr/bin/python3
"""
a module containing an empty class of geometry
"""


class BaseGeometry:
    """Base class representing base geometry."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'."""
        raise Exception("area() is not implemented")

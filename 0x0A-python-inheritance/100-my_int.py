#!/usr/bin/python3
"""
This module contains a class that inherits from int with inverted == and != operators.
"""


class MyInt(int):
    """Class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)

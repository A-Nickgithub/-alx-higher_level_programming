#!/usr/bin/python3
"""
This modules tells whether an object is an exact instance
of a class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of
    the specified class; otherwise False."""
    return type(obj) is a_class

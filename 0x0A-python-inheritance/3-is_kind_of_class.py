#!/usr/bin/python3
"""
This module tells us whether an object is an
instance of a class or an instance of a derived class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or inherited from, the specified class; otherwise False."""
    return isinstance(obj, a_class)

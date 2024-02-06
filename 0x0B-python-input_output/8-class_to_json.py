#!/usr/bin/python3
"""
This module returns a dictionary description of the object
"""


def class_to_json(obj):
    """
    take in the object and returns its
    dictionary representation
    """
    return obj.__dict__

#!/usr/bin/python3
import json
"""
This file contains a function that accepts a json string
and converts the string to a python object
"""


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string."""
    return json.loads(my_str)

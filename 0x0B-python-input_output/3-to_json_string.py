#!/usr/bin/python3
import json
"""
This script contains a function that accepts an object
and then converts the object to a json string
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)

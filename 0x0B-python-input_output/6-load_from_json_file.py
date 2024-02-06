#!/usr/bin/python3
import json
"""
in this file we will create a python object from
a json string
"""


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

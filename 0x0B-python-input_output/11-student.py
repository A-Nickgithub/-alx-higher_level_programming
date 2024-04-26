#!/usr/bin/python3
"""
we declare a class and initialize some
instance atrributes
and then we crate a function that basically returns
the dictionary representation of the class
this is achieved by use of the __dict__ attribute of the object
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

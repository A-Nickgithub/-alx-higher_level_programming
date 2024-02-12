#!/usr/bin/python3
"""
Base modules
"""
import json


class Base:
    """number of constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize

        Args:
        id(int) = id attribute
        """

    if id is None:
        Base.__nb_objects += 1
        id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string representation"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        json str representation of list_objs to a file

        """

    filename = cls.__name__ + ".json"

    with open(filename, "w") as jasonfile:
        if list_objs is None:
            jasonfile.write("[]")

        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jasonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        json string to dictionary

        """
        if json_string is None or json_string == "[]":
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """

        return a class initiated with attr already set

        Args:

        dictionary = key/value pair attribute to initialize

        """

        if cls.__name__ == 'Rectangle':

            dummy = cls(1, 1)

        else:

            dummy = clas(1)

            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):

        """
        return list of instance
        """

    filename = cls.__name__ + '.json'
    new = []

    try:
        with open(filename) as f:\
                content = f.read()

    except Exception as e:
        return new
    json_file = Base.from_json_string(content)
    for obj in json_file:
        new.append(cls.create(**obj))
        return new

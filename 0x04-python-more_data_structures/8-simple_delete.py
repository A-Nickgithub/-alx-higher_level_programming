#!/usr/bin/python3
def simple_delete(my_dictionary, key=""):
    if key in my_dictionary:
        my_dictionary.pop(key)
        return my_dictionary

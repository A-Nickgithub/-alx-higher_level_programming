#!/usr/bin/python3
def multiply_by_2(my_dictionary):
    new_dictionary = {}
    for key in my_dictionary:
        new_dictionary[key] = my_dictionary[key] * 2
        return new_dictionary

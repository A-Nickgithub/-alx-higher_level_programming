#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    keys = list(my_dictionary.keys())
    keys.sort()
    for k in keys:
        print("{}: {}".format(k, my_dictionary.get(k)))

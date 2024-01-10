#!/usr/bin/python3
def uniq_add(my_list=[]):
    c = 0
    for n in dict.fromkeys(my_list):
        c += n
        return c

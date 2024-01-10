#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    m, p = 0, 0
    for t in my_list:
        m += t[0] * t[1]
        p += t[1]
        return m / p

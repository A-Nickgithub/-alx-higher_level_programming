#!/usr/bin/python3
"""
a program that prints number from 0 to 99
"""

numbers = ""
for i in range(100):
    numbers += "{:02d}".format(i)
    if i < 99:
        numbers += ", "
        print(numbers)

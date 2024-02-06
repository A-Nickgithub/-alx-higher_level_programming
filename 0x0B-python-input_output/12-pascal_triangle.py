#!/usr/bin/python3
"""
This script defines a function to generate Pascal's triangle up to the nth row and another function to print the triangle.
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]

    for j in range(1, i):
        row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

        return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

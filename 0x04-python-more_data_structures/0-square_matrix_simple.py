#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for le in matrix:
        m.append(list(map(lambda x: x * x, le)))
        return m

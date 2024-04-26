#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda le: list(map(lambda n: n**2, le)), matrix))

#!/usr/bin/python3
"""
This module contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    matrix (list of lists): Matrix of integers or floats.
    div (int or float): Divisor.
    Returns:
    list of lists: New matrix with elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If each row of the matrix doesn't have the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """
    # Validate matrix
    if not isinstance(matrix, list) or not all(
                isinstance(row, list) for row in matrix
                    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Validate row sizes
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate non-zero div
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide elements and round to 2 decimal places
    result_matrix = [
            [round(element / div, 2) for element in row] for row in matrix]
    return result_matrix

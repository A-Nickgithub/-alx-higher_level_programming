#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.
    Args:
    matrix (list of list): A 2-dimensional array.
    Returns:
    list of list: A new matrix with each value being the square of the input.
    """
    new_matrix = []

    for row in matrix:
        new_row = [x**2 for x in row]
        new_matrix.append(new_row)

        return new_matrix
    # Example usage
    if __name__ == "__main__":
        matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]
        new_matrix = square_matrix_simple(matrix)

        print(new_matrix)
        print(matrix)

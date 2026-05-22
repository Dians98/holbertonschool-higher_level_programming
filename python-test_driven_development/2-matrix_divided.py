#!/usr/bin/python3
"""
This module provide
"""


def matrix_divided(matrix, div):
    """
        Divide the matrix by a given divider

        Args :
            matrix : array 
            divider : int
        Returns:
            the matrix divided by the given divider
        Ex:
             [[1, 2, 3],[4, 5, 6]] => [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    detect_matrix_type_value(matrix)
    detect_if_matrix_have_same_size(matrix)
    validate_divider(div)

    new = [row[:] for row in matrix]

    for item in range(len(new)):
        for i in range(len(new[item])):
            new[item][i] = round(new[item][i] / div, 2)

    return new


def detect_matrix_type_value(matrix):
    """
    Ensure values inside matrix are all int/float

    Args:
        matrix (array): _description_

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    not_int_or_float = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                not_int_or_float += 1

    if not_int_or_float > 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not detect_if_matrix_have_same_size(matrix):
        raise TypeError(
            "Each row of the matrix must have the same size")


def detect_if_matrix_have_same_size(matrix):
    """
    Detect if each row of the matrix has the same value
    Args:
        matrix (_type_): _description_

    Returns:
        _type_: _description_
    """
    size_matrix = []
    same_size = True

    for i in range(len(matrix)):
        size_matrix.append(len(matrix[i]))

    last_size = 0
    for i in range(len(size_matrix)):
        if i == 0:
            last_size = len(matrix[i])
        else:
            if (last_size != len(matrix[i])):
                same_size = False
            last_size = len(matrix[i])

    return same_size


def validate_divider(div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")

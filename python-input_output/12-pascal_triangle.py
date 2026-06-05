#!/usr/bin/python3
"""
This module is used for input/output exercices
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Initialize the current row with all 1s, matching the required size
        row = [1] * (i + 1)

        # Fill in the inner values (if any) based on the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

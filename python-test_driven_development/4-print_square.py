#!/usr/bin/python3
"""
This module provide a function that prints a square with the character #
"""


def print_square(size):
    """
    This function prints the square of a siez with #
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

#!/usr/bin/python3
"""
    This module provides a function to add two integers.

    Functions:
        add_integer(a, b=98): Returns the sum of two integers.
"""


def add_integer(a, b=98):
    """
        Adds two integers or floats (casted to int).

        Args:
            a (int, float): First number.
            b (int, float): Second number. Defaults to 98.

        Returns:
            int: The sum of a and b.

        Raises:
            TypeError: If a or b is not an integer or float.

        Examples:
            >>> add_integer(2, 3)
            5
            >>> add_integer(2)
            100
            >>> add_integer(2.5, 3.1)
            5
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a+b

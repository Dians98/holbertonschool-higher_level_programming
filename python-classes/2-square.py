#!/usr/bin/python3
""" 
This module is for an empty class that define square
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            pass
        if size < 0:
            raise ValueError("size must be >= 0")
            pass
        self.__size = size
        pass
    pass

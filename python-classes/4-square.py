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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
    pass

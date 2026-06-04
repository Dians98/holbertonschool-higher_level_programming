#!/usr/bin/python3
""" 
This module is for an empty class that define square
"""


class Square:
    """
    Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(n, int) and n > 0 for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) and n > 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

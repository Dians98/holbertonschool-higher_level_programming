#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with validation
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square
        """
        return self.__size * self.__size

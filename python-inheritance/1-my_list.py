#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
"""


class MyList(list):
    """
    A custom list class that adds sorted printing capabilities.
    """

    def print_sorted(self):
        """
        Prints the elements of the list sorted in ascending order
        without modifying the original list.
        """
        print(sorted(self))

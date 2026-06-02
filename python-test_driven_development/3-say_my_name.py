#!/usr/bin/python3
"""
This module provide a function for saying name
"""


def say_my_name(first_name, last_name):
    """
        Print full name
        Raise an error if last_name or first_name is not a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(
            "first_name must be a string or last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

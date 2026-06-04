#!/usr/bin/python3
"""
This module provides a lookup function for object attributes and methods.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)

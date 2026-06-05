#!/usr/bin/python3
"""
This module is used for input/output exercices
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string."""
    return json.loads(my_str)

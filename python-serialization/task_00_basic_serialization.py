#!/usr/bin/env python3
"""
Module for basic serialization and deserialization of Python dictionaries.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a specified JSON file.

    Args:
        data (dict): A Python dictionary containing data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Loads a JSON file and deserializes it back into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary containing the deserialized data.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)

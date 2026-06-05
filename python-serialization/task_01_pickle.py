#!/usr/bin/env python3
"""
Module for serializing and deserializing custom Python objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class representing a person with a name, age, and student status."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes a new CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a structured format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current object instance and saves it to a file.

        Returns None if an exception occurs during execution.
        """
        try:
            with open(filename, mode="wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns a CustomObject instance from a file.

        Returns None if the file doesn't exist, is malformed, or can't be read.
        """
        try:
            with open(filename, mode="rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception):
            return None

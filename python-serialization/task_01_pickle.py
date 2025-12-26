#!/usr/bin/env python3
"""Module for serializing and deserializing CustomObject using pickle."""


import pickle


class CustomObject:
    """Custom object that can be serialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        return None

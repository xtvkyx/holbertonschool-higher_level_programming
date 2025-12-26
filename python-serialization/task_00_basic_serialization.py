#!/usr/bin/env python3
"""Basic serialization module for saving and loading dictionaries as JSON."""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.
    If the file exists, it will be overwritten.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it
    into a Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

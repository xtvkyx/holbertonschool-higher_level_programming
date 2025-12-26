#!/usr/bin/python3
"""Module that converts a class instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__

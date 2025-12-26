#!/usr/bin/python3
"""Module that defines a Student class with serialization support."""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)

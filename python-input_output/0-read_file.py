#!/usr/bin/python3
"""Module that contains a function to read a text file."""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

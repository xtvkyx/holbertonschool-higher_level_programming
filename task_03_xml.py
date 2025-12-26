#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = "" if value is None else str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.
    Note: XML stores everything as text, so values are returned as strings.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text if child.text is not None else ""

    return result

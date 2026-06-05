#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries to/from XML format.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary containing data to serialize.
        filename (str): The destination file path.
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Reads XML data from a file and returns a deserialized Python dictionary.

    Args:
        filename (str): The XML file path to parse.

    Returns:
        dict: A dictionary reconstructed from the XML data.
    """
    try:

        tree = ET.parse(filename)
        root = tree.getroot()

        reconstructed_dict = {}

        for child in root:
            val = child.text

            if val is None:
                val = ""
            elif val.lower() == "true":
                val = True
            elif val.lower() == "false":
                val = False
            else:
                try:

                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:

                    pass

            reconstructed_dict[child.tag] = val

        return reconstructed_dict

    except FileNotFoundError:
        return None

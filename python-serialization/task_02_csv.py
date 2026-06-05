#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file into JSON format and writes it to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:

        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:

            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:

            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, Exception):
        return False

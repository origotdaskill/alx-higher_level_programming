#!/usr/bin/python3
"""Module to save Python objects to JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file in JSON format.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

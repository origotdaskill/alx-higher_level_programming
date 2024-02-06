#!/usr/bin/python3
"""Module to convert an instance of a class to a JSON-compatible dictionary."""


def class_to_json(obj):
    """
    Convert an instance of a class to a JSON-compatible dictionary.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object.
    """
    json_dict = {}

    # Iterate through the attributes of the object
    for key, value in obj.__dict__.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict

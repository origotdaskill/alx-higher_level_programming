#!/usr/bin/python3
"""Simple delete by key"""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary."""
    a_dictionary.pop(key, None)
    return a_dictionary

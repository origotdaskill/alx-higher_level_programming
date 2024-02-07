#!/usr/bin/python3
"""
Module: 2-append_write

This module provides a function to append a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)

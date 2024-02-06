#!/usr/bin/python3
"""Module 1-write_file"""


def write_file(filename="", text=""):
    """Writes to file and returns number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

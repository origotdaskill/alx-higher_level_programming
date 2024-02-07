#!/usr/bin/python3
"""Module to append text to a file after specific lines."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing string.

    Args:
        filename (str):name of the file to append to.
        search_string (str):string to search for in each line.
        new_string (str): string to insert after each line containing string.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

#!/usr/bin/python3
"""Search and replace"""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = [replace if x == search else x for x in my_list]
    return new_list

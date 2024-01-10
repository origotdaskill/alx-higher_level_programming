#!/usr/bin/python3
"""Unique add"""


def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    unique_set = set(my_list)
    result = sum(unique_set)
    return result

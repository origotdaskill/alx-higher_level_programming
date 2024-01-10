#!/usr/bin/python3
"""Multiply list using map"""


def multiply_list_map(my_list=[], number=0):
    """Return a new list with all values multiplied by a number using map."""
    return list(map(lambda x: x * number, my_list))

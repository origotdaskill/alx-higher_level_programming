#!/usr/bin/python3
"""Only differents"""


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set


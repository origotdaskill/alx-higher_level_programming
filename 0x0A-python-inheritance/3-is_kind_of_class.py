#!/usr/bin/python3
"""Module with is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited from a_class"""
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Module with inherits_from function"""


def inherits_from(obj, a_class):
    """Check if obj inherits (directly or indirectly) from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

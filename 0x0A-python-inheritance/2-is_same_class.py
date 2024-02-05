#!/usr/bin/python3
"""Module with is_same_class function"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of the specified class"""
    return type(obj) is a_class

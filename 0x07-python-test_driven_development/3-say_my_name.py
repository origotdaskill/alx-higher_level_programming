#!/usr/bin/python3
"""
Prints My name is <first name> <last name>.

Prototype: def say_my_name(first_name, last_name="")
first_name and last_name must be strings otherwise, raise a TypeError
exception with the message first_name must be a string or last_name
must be a string
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
    - first_name (str): The first name.
    - last_name (str, default: ""): The last name.

    Raises:
    - TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

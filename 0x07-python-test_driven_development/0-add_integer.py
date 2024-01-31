#!/usr/bin/python3
"""
Adds two integers.

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError
with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    - a (int or float): The first number.
    - b (int or float, default: 98): The second number.

    Raises:
    - TypeError: If a or b is not an integer or float.

    Returns:
    - int: The addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

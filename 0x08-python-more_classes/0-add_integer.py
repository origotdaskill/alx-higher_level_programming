#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float): The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

# Test cases
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))

try:
    print(add_integer(4, "School"))
except TypeError as e:
    print(e)

try:
    print(add_integer(None))
except TypeError as e:
    print(e)

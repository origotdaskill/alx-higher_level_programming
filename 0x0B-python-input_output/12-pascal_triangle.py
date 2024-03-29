#!/usr/bin/python3
"""Module to generate and print Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """Print the triangle.

    Args:
        triangle (list): A list of lists representing Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

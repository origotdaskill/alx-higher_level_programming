#!/usr/bin/python3
"""Defines the MagicClass class."""

import math


class MagicClass:
    """Represents a magic class."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass class."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes the area of the magic class."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference of the magic class."""
        return 2 * math.pi * self.__radius

#!/usr/bin/python3
"""Module with MyList class"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))

    def __str__(self):
        """Override the string representation of MyList"""
        return super().__str__()

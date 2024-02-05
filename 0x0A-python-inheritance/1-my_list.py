#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A class that inherits from list.

    Public Methods:
    - print_sorted(): Prints the list sorted in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))

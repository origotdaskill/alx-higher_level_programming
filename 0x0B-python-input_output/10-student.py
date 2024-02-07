#!/usr/bin/python3
"""Module to define a Student class."""


class Student:
    """Class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr)or attr in attrs 
                    if hasattr(self, attr)
                    }

#!/usr/bin/python3
"""Module to define a Student class."""


class Student:
    """Class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student.

        Args:
            attrs (list): A list of attributes to include in the dictionary.
                          If None, all attributes are included.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                    attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)
                    }

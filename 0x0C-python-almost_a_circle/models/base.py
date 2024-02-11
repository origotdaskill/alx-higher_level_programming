#!/usr/bin/python3
"""Module for Base class"""

import json


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with id attribute"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            list_dicts_sorted = [dict(sorted(d.items(),
                                             key=lambda item: item[0]))
                                 for d in list_dicts]
            file.write(Base.to_json_string(list_dicts_sorted))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [
                        cls.create(**dictionary)
                        for dictionary in dictionaries
                        ]
        except FileNotFoundError:
            return []

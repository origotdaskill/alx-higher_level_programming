#!/usr/bin/python3
"""Module for Base class"""

import json
import csv
import turtle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to CSV format and saves it to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV data from a file and returns a list of objects"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                objs = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(*map(int, row))
                    elif cls.__name__ == 'Square':
                        obj = cls(*map(int, row))
                    objs.append(obj)
                return objs
        except FileNotFoundError:
            return []
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""

        # Create a Turtle object
        screen = turtle.Screen()
        screen.title("Shapes Drawing")
        screen.setup(width=600, height=400)
        t = turtle.Turtle()

        # Draw rectangles
        t.penup()
        t.color("blue")
        for rect in list_rectangles:
            t.goto(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.penup()

        # Draw squares
        t.color("red")
        for square in list_squares:
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
            t.penup()

        # Close the turtle graphics window on click
        screen.exitonclick()

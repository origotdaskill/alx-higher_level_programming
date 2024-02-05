#!/usr/bin/python3
"""Module 8-rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes an instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

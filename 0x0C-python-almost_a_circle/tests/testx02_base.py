#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Base.save_to_file([r1, r2])

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r") as file:
            actual_output = file.read()

        expected_output = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, \
{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'

        self.assertEqual(actual_output, expected_output)


        self.assertEqual(actual_output, expected_output)

    def tearDown(self):
        """Clean up files created by tests"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
import io
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_constructor(self):
        """Test the constructor of the Rectangle class"""
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_area(self):
        """Test the area method of the Rectangle class"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test the display method of the Rectangle class"""
        rect = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rect.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ method of the Rectangle class"""
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(str(rect), "[Rectangle] (100) 1/2 - 5/10")

    def test_update(self):
        """Test the update method of the Rectangle class"""
        rect = Rectangle(5, 10, 1, 2, 100)
        rect.update(20, 6, 12, 3, 4)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Rectangle class"""
        rect = Rectangle(5, 10, 1, 2, 100)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 100, 'width': 5, 'height': 10, 'x': 1, 'y': 2})

if __name__ == '__main__':
    unittest.main()

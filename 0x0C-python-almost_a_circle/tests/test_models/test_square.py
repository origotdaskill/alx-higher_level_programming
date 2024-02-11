#!/usr/bin/python3
"""Test cases for the Square class"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_constructor(self):
        """Test the constructor of the Square class"""
        square = Square(5, 1, 2, 100)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 100)

    def test_size_property(self):
        """Test the size property of the Square class"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_update_method(self):
        """Test the update method of the Square class"""
        square = Square(5, 1, 2, 100)
        square.update(20, 10, 3, 4)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_str_method(self):
        """Test the __str__ method of the Square class"""
        square = Square(5, 1, 2, 100)
        self.assertEqual(str(square), "[Square] (100) 1/2 - 5")

if __name__ == '__main__':
    unittest.main()

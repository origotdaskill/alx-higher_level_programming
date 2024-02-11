#!/usr/bin/python3
"""Unittest for Base class create method."""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestCreateMethod(unittest.TestCase):
    """Test cases for create method."""

    def test_create_rectangle(self):
        """Test create method with Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)

    def test_create_square(self):
        """Test create method with Square."""
        s1 = Square(4, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s1.size, s2.size)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)


if __name__ == "__main__":
    unittest.main()

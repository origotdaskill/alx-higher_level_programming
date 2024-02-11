# tests/test_square.py

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_size_getter(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(10)
        self.assertEqual(s2.size, 10)

    def test_size_setter(self):
        s1 = Square(5)
        s1.size = 8
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.width, 8)
        self.assertEqual(s1.height, 8)

        s2 = Square(10)
        s2.size = 3
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)

    def test_size_setter_invalid_value(self):
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1.size = "9"

        s2 = Square(10)
        with self.assertRaises(ValueError):
            s2.size = -2

if __name__ == '__main__':
    unittest.main()

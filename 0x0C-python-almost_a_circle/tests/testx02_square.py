# tests/test_square.py

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_update_with_args(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(1, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        s1.update(1, 2, 3)
        self

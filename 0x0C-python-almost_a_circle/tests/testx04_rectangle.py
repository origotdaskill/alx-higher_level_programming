# tests/test_rectangle.py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")


if __name__ == '__main__':
    unittest.main()

# tests/test_rectangle.py

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle(10, "2")
        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(ValueError) as cm:
            r2 = Rectangle(-10, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r3 = Rectangle(10, 2)
            r3.width = "invalid"
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            r4 = Rectangle(10, 2)
            r4.x = -1
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as cm:
            r5 = Rectangle(10, 2, 3, "invalid")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            r6 = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")


if __name__ == '__main__':
    unittest.main()

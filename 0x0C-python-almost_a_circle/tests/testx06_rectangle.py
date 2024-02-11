# testx06_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_update(self):
        r = Rectangle(5, 5, 1, 0)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

# Add other test cases for Rectangle class

if __name__ == '__main__':
    unittest.main()
# testx06_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_update(self):
        r = Rectangle(5, 5, 1, 0)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

# Add other test cases for Rectangle class

if __name__ == '__main__':
    unittest.main()


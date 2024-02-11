# testx02_base.py

import unittest
import os
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))  # Check if file exists

# Add other test cases for saving to file

if __name__ == '__main__':
    unittest.main()

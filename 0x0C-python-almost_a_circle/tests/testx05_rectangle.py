# tests/testx05_rectangle.py

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io

class TestRectangle(unittest.TestCase):
    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"  # Include newline characters at the beginning
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()


# tests/test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_constructor(self):
        b1 = Base()
        self.assertIsNotNone(b1.id)

        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

if __name__ == '__main__':
    unittest.main()

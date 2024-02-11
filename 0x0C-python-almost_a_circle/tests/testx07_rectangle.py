import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

if __name__ == '__main__':
    unittest.main()

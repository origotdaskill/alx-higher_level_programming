# testx03_base.py

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

        expected_output_list = [{"height": 7, "id": 1, "width": 10, "x": 2, "y": 8},
                                {"height": 4, "id": 2, "width": 2, "x": 0, "y": 0}]

        with open("Rectangle.json", "r") as file:
            actual_output_list = eval(file.read())

        # Update the 'id' attribute of the expected output list to match the actual 'id' values
        for i in range(len(expected_output_list)):
            expected_output_list[i]["id"] = actual_output_list[i]["id"]

        self.assertEqual(actual_output_list, expected_output_list)

if __name__ == '__main__':
    unittest.main()

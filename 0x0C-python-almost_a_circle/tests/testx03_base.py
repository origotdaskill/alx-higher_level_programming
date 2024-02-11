import unittest
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_save_to_file(self):
        """Test save_to_file method"""

        # Test with Rectangle objects
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            actual_output = file.read()
        expected_output = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}, {"x": 0, "y": 0, "id": 2, "width": 2, "height": 4}]'

        # Convert JSON strings to Python lists
        actual_output_list = eval(actual_output)
        expected_output_list = eval(expected_output)

        # Sort the lists of dictionaries
        actual_output_list.sort(key=lambda x: x["id"])
        expected_output_list.sort(key=lambda x: x["id"])

        # Compare the sorted lists
        self.assertEqual(actual_output_list, expected_output_list)

if __name__ == "__main__":
    unittest.main()

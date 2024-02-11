import unittest
import os
from models.rectangle import Rectangle
from models.square import Square


class TestLoadFromFile(unittest.TestCase):
    """Test cases for load_from_file method"""

    @classmethod
    def setUpClass(cls):
        """Create a dummy Rectangle file"""
        filename = "Rectangle.json"
        Rectangle.save_to_file([])
        cls.rectangle_filename = filename

    @classmethod
    def tearDownClass(cls):
        """Remove the dummy Rectangle file if it exists"""
        if os.path.exists(cls.rectangle_filename):
            os.remove(cls.rectangle_filename)

    def tearDown(self):
        """Remove the dummy Rectangle file after each test if it exists"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_empty_file(self):
        """Test load_from_file method with empty file"""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_nonexistent_file(self):
        """Test load_from_file method with nonexistent file"""
        # Ensure the file does not exist
        filename = "NonexistentFile.json"
        if os.path.exists(filename):
            os.remove(filename)
        # Attempt to load from a nonexistent file
        rectangles = Rectangle.load_from_file()
        # Ensure that an empty list is returned
        self.assertEqual(rectangles, [])

    def test_load_from_file_existing_file(self):
        """Test load_from_file method with existing file"""
        # Create some rectangles
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        # Save the rectangles to file
        Rectangle.save_to_file([r1, r2])
        # Load the rectangles from file
        rectangles = Rectangle.load_from_file()
        # Ensure that the loaded rectangles match the originals
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles[1].to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_single_dict(self):
        dictionary = {"id": 1, "name": "Alice"}
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}]')

    def test_to_json_string_multiple_dicts(self):
        dictionaries = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ]
        json_string = Base.to_json_string(dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]')

if __name__ == '__main__':
    unittest.main()

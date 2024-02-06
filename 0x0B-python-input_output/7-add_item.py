#!/usr/bin/python3
"""
Script to add command-line arguments to a Python list and save them to a JSON file.
"""

import sys
from json import load, dump

def load_from_json_file(filename):
    """Load a JSON file and return its content."""
    with open(filename, 'r') as f:
        return load(f)

def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, 'w') as f:
        dump(my_obj, f)

# Check if the add_item.json file exists
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, "add_item.json")

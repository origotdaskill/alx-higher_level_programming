#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)

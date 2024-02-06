#!/usr/bin/python3

def append_write(filename="", text=""):
    """Append a string to the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"Error: {e}")
        return 0

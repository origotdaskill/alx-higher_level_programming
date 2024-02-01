#!/usr/bin/python3
"""Function to print text with 2 new lines after '.', '?', and ':'
"""


def text_indentation(text):
    """Prints the text with 2 new lines after '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in ['.', '?', ':']:
            print("\n")
            if idx + 1 < len(text) and text[idx + 1] == ' ':
                idx += 1
        idx += 1

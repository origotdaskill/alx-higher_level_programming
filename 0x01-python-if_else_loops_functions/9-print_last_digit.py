#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the last digit of a number.
    Args:
        number: The number to extract the last digit from.
    Returns:
        The last digit of the number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

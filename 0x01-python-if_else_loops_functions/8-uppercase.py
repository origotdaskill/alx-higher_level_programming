#!/usr/bin/python3

def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.
    Args:
        str: The string to be printed in uppercase.
    """
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

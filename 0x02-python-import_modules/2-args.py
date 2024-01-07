#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # subtract 1 to exclude the script name
    args = argv[1:] if num_args > 0 else []

    print("{} argument{}{}".format(num_args, 's' if num_args != 1 else '', ':' if num_args > 0 else '.'))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))

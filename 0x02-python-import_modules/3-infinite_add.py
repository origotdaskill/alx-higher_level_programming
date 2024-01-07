#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    total_sum = 0

    for arg in args:
        total_sum += int(arg)

    print(total_sum)

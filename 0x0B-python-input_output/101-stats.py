#!/usr/bin/python3
"""Module to parse log lines and compute statistics."""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics for file size and status codes.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the count of each status.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parses a line and extracts the status code and file size.

    Args:
        line (str): The input line to parse.

    Returns:
        tuple: A tuple containing the status code (int) and file size (int).
    """
    parts = line.split()
    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size


def main():
    """Main function to read log lines from stdin and compute statistics."""
    total_size = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    try:
        for i, line in enumerate(sys.stdin, start=1):
            status_code, file_size = parse_line(line)
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            if i % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary with status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """
    Parses a line and updates the total size and status codes.

    Args:
        line (str): The input line.
        total_size (int): Total file size.
        status_codes (dict): Dictionary with status codes and their counts.

    Returns:
        Tuple: (Updated total size, Updated status codes)
    """
    tokens = line.split()
    if len(tokens) >= 9:
        total_size += int(tokens[-1])
        status_code = tokens[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    return total_size, status_codes

def main():
    """
    Main function to read stdin, parse lines, and print statistics.
    """
    total_size = 0
    status_codes = {}

    try:
        for count, line in enumerate(sys.stdin, start=1):
            total_size, status_codes = parse_line(line, total_size, status_codes)
            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

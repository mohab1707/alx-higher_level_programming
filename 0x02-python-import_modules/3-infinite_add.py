#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    total = 0

    for arg in args:
        total += int(arg)

    print("{}".format(total))

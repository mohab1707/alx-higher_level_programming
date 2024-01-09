#!/usr/bin/python3
"""
Module with a function to read and print the
content of a text file.
"""

def read_file(filename=""):
    """
    Read and print the content of a text file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())

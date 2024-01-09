#!/usr/bin/python3
"""
Module with a function append_after to insert a line of text
after each line containing a specific string in a file.
"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The specific string to search for.
        new_string (str): The line of text to insert.

    Returns:
        None
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

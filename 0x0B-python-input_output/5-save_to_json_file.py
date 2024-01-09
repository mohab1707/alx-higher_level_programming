#!/usr/bin/python3
"""
Module with a function to write an object
to a text file using a JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized
        and written to the file.
        filename (str): The name of the file to be written.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
        

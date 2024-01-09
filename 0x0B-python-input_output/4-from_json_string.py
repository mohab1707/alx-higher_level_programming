#!/usr/bin/python3
"""
Module with a function to return an object
(Python data structure) represented by a JSON string.
"""

import json

def from_json_string(my_str):
    """
    Return an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string
        to be converted to a Python object.

    Returns:
        obj: The Python object represented by
        the JSON string.
    """
    return json.loads(my_str)

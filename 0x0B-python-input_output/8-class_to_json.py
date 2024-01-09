#!/usr/bin/python3
"""
Module with a function to return
the dictionary description for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Return the dictionary description
    for JSON serialization of an object.

    Args:
        obj: The object for which
        to generate the dictionary description.

    Returns:
        dict: The dictionary description
        for JSON serialization.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        return obj.__str__()

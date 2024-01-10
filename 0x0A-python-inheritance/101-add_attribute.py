#!/usr/bin/python3
"""
Module with a function add_attribute.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception with the message "can't add new attribute"
    if the object can't have a new attribute.

    Args:
        obj: The object to which the attribute is to be added.
        name (str): The name of the attribute.
        value: The value of the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)


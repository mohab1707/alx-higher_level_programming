#!/usr/bin/python3
"""
Module with a function that returns
the list of available attributes and
methods of an object.
"""


def lookup(obj):
    """
    Returns a list object
    """
    return dir(obj)

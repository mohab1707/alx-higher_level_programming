#!/usr/bin/python3
"""
Module: 1-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """
    Defines a square with a private instance attribute size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private and accessible only through
            the getter and setter methods.
        """
        self.__size = size

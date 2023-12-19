#!/usr/bin/python3
"""
Module: 2-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """
    Defines a square with a private instance attribute size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

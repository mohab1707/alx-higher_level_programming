#!/usr/bin/python3
"""
Module with a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)


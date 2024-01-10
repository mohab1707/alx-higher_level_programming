#!/usr/bin/python3
"""
Module with a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior.

        Args:
            other: The object to compare.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior.

        Args:
            other: The object to compare.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)


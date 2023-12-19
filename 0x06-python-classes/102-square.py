#!/usr/bin/python3
"""
Module: 102-square
Defines a class Square with private instance attributes size.
"""


class Square:
    """
    Defines a square with private instance attributes size.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (number): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size.

        Args:
            value: The size to be set (must be a number).

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the area is less than the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the area is less than or equal to the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the area is greater than the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison method.

        Args:
            other: The other square to compare.

        Returns:
            bool: True if the area is greater than or equal to the other square, False otherwise.
        """
        return self.area() >= other.area()

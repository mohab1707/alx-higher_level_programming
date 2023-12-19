#!/usr/bin/python3
"""
Module: 103-magic_class
Defines a Python class MagicClass that replicates the behavior of
a given Python bytecode.
"""

import math

class MagicClass:
    """
    Python class that replicates the behavior of the given bytecode.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (number): The radius value.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius

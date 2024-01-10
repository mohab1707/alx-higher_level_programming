#!/usr/bin/python3
"""
Module with an improved class BaseGeometry.
"""


class BaseGeometry:
    """
    An improved class with public instance methods.
    """

    def area(self):
        """
        Raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer
        - If value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


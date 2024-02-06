#!/usr/bin/python3
"""
Module with a class BaseGeometry.
"""


class BaseGeometry:
    """
    BaseGeometry class provides a base for geometry-related classes.
    """
    def area(self):
        """
        Public instance method that raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates the value to be
        an integer greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

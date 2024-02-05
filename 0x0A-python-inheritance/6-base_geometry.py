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

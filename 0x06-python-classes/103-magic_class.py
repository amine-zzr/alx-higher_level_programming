#!/usr/bin/python3

"""
Module: magic_class

This module defines the MagicClass class, which represents a circle and
    provides methods to calculate its area and circumference.
"""

import math


class MagicClass:
    def __init__(self, radius):
        """
        Constructor method for MagicClass.

        Parameters:
        - radius (int or float): The radius of the circle.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.
        """
        return 2 * math.pi * self.__radius

#!/usr/bin/python3
"""
MagicClass Module
This module defines the MagicClass class, which represents a circle and provides
    methods to calculate its area and circumference.
"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Parameterss:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.

        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.

        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.

        """
        return 2 * math.pi * self.__radius

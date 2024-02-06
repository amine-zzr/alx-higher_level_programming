#!/usr/bin/python3
"""
This Module defines Rectangle class.
"""

BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """
    Rectangle class inherits from BaseGeometry.

    Public Methods:
    - __init__(self, width, height): Instantiates a Rectangle
                                     object with width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height.

        Parameters:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

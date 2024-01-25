#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class represents a square.

    Attributes:
    __size (int): Private instance attribute representing
                  the size of the square.
    """
    def __init__(self, size=0):
        """ This is the constructor method for the Square class.

        Parameters:
        - size (int): Size of the square. default is 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Public method to calculate and return the area of the square.

        Returns:
        int: Area of the square.
        """

        return self.__size ** 2

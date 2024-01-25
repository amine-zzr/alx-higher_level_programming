#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class represents a square.

    Attributes:
    __size (int): Private instance attribute representing the size of the square.
    """
    def __init__(self, size):
        """ This is the constructor method for the Square class.

        Parameters:
        - size (int): Size of the square (no type/value verefication).
        """
        self.__size = size

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
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square."
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
        - value (int): Size to set.

        Raises:
        - TypeError: if size is not an integer.
        - ValueError: if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Public method to calculate and return the area of the square.

        Returns:
        int: Area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Public method to print in stdout the square with the character #.
        If size is 0, print an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

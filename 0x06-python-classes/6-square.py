#!/usr/bin/python3

"""This module defines the Square class."""


class Square:
    """This class represents a square.

    Attributes:
    __size (int): Private instance attribute representing
                  the size of the square.
    __position (tuple): Private instance attribute representing
                        the position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """ This is the constructor method for the Square class.

        Parameters:
        - size (int): Size of the square. default is 0.
        - position (tuple): Position of the square. default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Parameters:
        - value (tuple): position to set.

        Raises:
        - TypeError: if position is not a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(coord, int)
                    and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
        position is used to add spaces before printing the square.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

#!/usr/bin/python3
'''
This Module intializes the Square class.
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square class inherits from Rectangle.
    '''

    def __init__(self, size):
        '''
        Initializes a Square object with size.

        Parameters:
        - size: Size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.
        '''

        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        '''
        Returns the string representation of the square.
        '''

        return "[Rectangle] {}/{}".format(self.__size, self.__size)

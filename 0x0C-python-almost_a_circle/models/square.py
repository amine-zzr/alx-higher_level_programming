#!/usr/bin/python3
'''
This Module defines a Square Class.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class, inherits from Rectangle.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initialize a Square object.
        '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Override the string representation of the Square.
        '''

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

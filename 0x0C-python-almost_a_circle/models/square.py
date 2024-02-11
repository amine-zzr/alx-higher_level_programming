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

    @property
    def size(self):
        '''Getter method for size attribute.'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter method for size attribute.'''
        self.width = value
        self.height = value

    def __str__(self):
        '''
        Override the string representation of the Square.
        '''

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''
        Update attributes of the Square.
        '''

        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                super().update(**kwargs)

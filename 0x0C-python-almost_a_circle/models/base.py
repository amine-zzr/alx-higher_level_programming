#!/usr/bin/python3
'''
This Module initializes a class Base as the base class of all other classes.
'''


class Base:
    '''
    Base class for managing IDs in the project.

    Attributes:
    - __nb_objects (int): Private class attribute to
                          track the number of objects.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initialize a Base object with a unique ID.

        Args:
        - id (int, optional): If provided, sets the object ID to the given
                              value.
                              If not provided, increments the object counter
                              and assigns the new value.
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

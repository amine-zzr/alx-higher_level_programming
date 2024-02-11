#!/usr/bin/python3

import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Return the JSON string representation of list_dictionaries.
        '''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Write the JSON string representation of list_objs to a file.
        '''

        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_str = cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs])
                file.write(json_str)

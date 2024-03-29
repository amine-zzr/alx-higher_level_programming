#!/usr/bin/python3

'''
This Module initializes a class Base as the base class of all other classes.
'''

import csv
import json


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

    @staticmethod
    def from_json_string(json_string):
        '''
        Return the list of dictionaries represented by json_string.
        '''

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Return an instance with all attributes set based on dictionary.
        '''

        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError('Unsupported class')

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances
        '''

        filename = cls.__name__ + '.json'

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                if json_string:
                    dictionaries = cls.from_json_string(json_string)
                    instances = [cls.create(**d) for d in dictionaries]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Write the CSV serialization of a list of objects to a file.
        '''

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow(
                            [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''
        Return a list of classes instantiated from a CSV file.
        '''

        filename = cls.__name__ + '.csv'
        objects = []
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(*map(int, row[1:]), id=int(row[0]))
                    elif cls.__name__ == 'Square':
                        obj = cls(*map(int, row[1:]), id=int(row[0]))
                    objects.append(obj)
        except FileNotFoundError:
            pass

        return objects

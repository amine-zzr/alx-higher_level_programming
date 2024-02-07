#!/usr/bin/python3
'''
Module to define Student class
'''


class Student:
    '''
    Defines a student.
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Initialize a student with first_name, last_name, and age.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieve a dictionary representation of a Student instance.
        '''

        if attrs is None:
            return vars(self)
        else:
            return {
                attr: getattr(self, attr) for attr in attrs if hasattr(
                              self, attr)
            }

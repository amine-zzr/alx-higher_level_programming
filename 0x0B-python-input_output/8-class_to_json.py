#!/usr/bin/python3
'''
This Module defines a function that returns the dictionary
description with simple data structures
'''


def class_to_json(obj):
    '''
    Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: An instance of a class with attributes that are serializable.

    Returns:
        dict: A dictionary containing the attributes of the object.
    '''

    attributes = obj.__dict__

    serializable_attributes = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[attr] = value

    return serializable_attributes

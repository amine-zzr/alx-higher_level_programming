#!/usr/bin/python3
'''
This Module define a function that creates an object from a JSON file.
'''

import json


def load_from_json_file(filename):
    '''
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object represented by the JSON file.
    '''

    with open(filename, "r") as file:
        return json.load(file)

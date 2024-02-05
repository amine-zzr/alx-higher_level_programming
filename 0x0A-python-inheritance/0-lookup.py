#!/usr/bin/python3
"""
defines a function that returns a list of an object methods and objects.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object for which to retrieve attributes and methods.

    Returns:
    A list containing the names of attributes and methods of the object.
    """
    return (dir(obj))

#!/usr/bin/python3
"""
Module: say_my_name

This module provides a function to print a message with
    the provided first name and last name.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a message with the provided first name and last name.

    Parameters:
    first_name (str): The first name to be included in the message.
    last_name (str, optional): The last name to be included in
                               the message. Defaults to an empty string.

    Raises:
    TypeError: If first_name is not a string.
    TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

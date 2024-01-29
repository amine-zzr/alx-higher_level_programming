#!/usr/bin/python3
"""
Module: integer_adder

This module provides a function for adding two integers.

Functions:
    add_integer(a, b=98): Adds two integers and returns the result.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: the sum of a and b.

    Raises:
        TypeError: if a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

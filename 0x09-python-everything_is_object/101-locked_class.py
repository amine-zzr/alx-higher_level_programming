#!/usr/bin/python3
"""Defin a class, LockedClass"""


class LockedClass:
    """A class that restricts dynamic creation of instance attributes.

    Only allows the creation of the 'first_name' attribute.
    """
    __slots__ = ['first_name']

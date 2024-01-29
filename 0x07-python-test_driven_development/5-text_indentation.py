#!/usr/bin/python3
"""
Module: text_indentation

This module provides a function to print a text with 2 new lines
    after each of these characters: ., ? and :.

Functions:
    text_indentation(text): Prints a text with 2 new lines
        after each of these characters: ., ? and :.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ") for line in text.split(char)])

    print(text, end="")

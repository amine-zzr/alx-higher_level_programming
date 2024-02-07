#!/usr/bin/python3
'''
This Module defines a function to append a string at the end of a file.
'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The path of the file to append to.
                        Defaults to an empty string.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    '''

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

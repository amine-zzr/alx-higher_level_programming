#!/usr/bin/python3
'''
This Module defines a function to write in a file.
'''


def write_file(filename="", text=""):
    '''
    Writes a string to a text file

    Args:
        filename (str): The path of the file to write.
                        Defaults to an empty string.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    '''

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

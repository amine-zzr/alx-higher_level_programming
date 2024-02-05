#!/usr/bin/python3
"""
defines a class that has a public method to print a list in sorted oreder.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).
        """
        print(sorted(self))

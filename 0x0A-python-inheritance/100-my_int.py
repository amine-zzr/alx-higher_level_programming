#!/usr/bin/python3
'''
This module defines MyInt class.
'''


class MyInt(int):
    '''
    MyInt class inherits from int.
    '''

    def __eq__(self, other):
        '''
        Overrides the equality operator.

        Parameters:
        - other: The value to compare with.
        '''

        return super().__ne__(other)

    def __ne__(self, other):
        '''
        Overrides the inequality operator.

        Parameters:
        - other: The value to compare with.
        '''

        return super().__eq__(other)

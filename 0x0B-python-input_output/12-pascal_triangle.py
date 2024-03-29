#!/usr/bin/python3
'''
This Module defines a function that prints the pascal's triangle.
'''


def pascal_triangle(n):
    '''
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle up to the nth row.
    '''

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle

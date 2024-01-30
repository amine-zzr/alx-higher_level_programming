#!/usr/bin/python3
"""
Matrix Multiplication Module

This module provides a function for multiplying two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The resulting matrix after multiplying m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b
            is not a list of lists.
        ValueError: If m_a or m_b is empty, or if one element of the matrices
            is not an integer or a float,
            or if each row of m_a is not of the same size,
            or if each row of m_b is not of the same size,
            or if m_a and m_b cannot be multiplied.
    """

    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not matrix or any(not row for row in matrix):
            raise ValueError(f"{name} can't be empty")
        if any(not isinstance(
                    num, (int, float)) for row in matrix for num in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"each row of {name} must be of the same size")

        if len(m_a[0]) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

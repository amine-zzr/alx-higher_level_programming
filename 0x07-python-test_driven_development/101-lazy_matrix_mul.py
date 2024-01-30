#!/usr/bin/python3
"""
Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (list of lists): The first matrix represented as a list of lists.
    - m_b (list of lists): The second matrix represented as a list of lists.

    Returns:
    - list of lists: The result of matrix multiplication as a list of lists.
    """

    return np.matmul(m_a, m_b)

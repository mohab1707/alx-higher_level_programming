#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices.

"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        ValueError: If m_a or m_b is empty or not a rectangle.
        TypeError: If one element of m_a or m_b is not an integer or a float.
        ValueError: If m_a and m_b can't be multiplied.

    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a) or len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row) or not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

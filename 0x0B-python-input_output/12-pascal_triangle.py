#!/usr/bin/python3
"""
Module with a function pascal_triangle
that returns Pascal's triangle of n.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows (n).

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
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

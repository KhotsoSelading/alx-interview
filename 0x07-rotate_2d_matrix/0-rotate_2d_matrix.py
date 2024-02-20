#!/usr/bin/python3
"""
Topic: Rotate 2d Matrix
Author: Khotso Selading
Date: 19-02-2024
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
    None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

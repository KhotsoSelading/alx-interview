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
    matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]

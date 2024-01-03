#!/usr/bin/python3

"""
Author: Khotso Selading
Date: 03-01-2024
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing
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

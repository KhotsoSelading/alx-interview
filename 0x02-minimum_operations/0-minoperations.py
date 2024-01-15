#!/usr/bin/python3
"""
Topic: Lockboxes
Author: Khotso Selading
Date: 15-01-2024
"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if (n < 2):
        return 0

    total_operations = 0
    divisor_candidate = 2

    while divisor_candidate <= n:
        if n % divisor_candidate == 0:
            total_operations += divisor_candidate
            n = n / divisor_candidate
            divisor_candidate -= 1
        divisor_candidate += 1

    return total_operations

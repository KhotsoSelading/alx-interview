#!/usr/bin/python3
"""
Topic: Prime Game
Author: Khotso Selading
Date: 10-03-2024
"""


def is_prime(num):
    """
    Finds prime number
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Finds the winner
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        primes_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

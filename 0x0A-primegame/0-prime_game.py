#!/usr/bin/python3
"""
Topic: Prime Game
Author: Khotso Selading
Date: 10-03-2024
"""


def sieve_of_eratosthenes(n):
    """
    Finds prime numbers
    """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]


def is_winner(x, nums):
    """
    Chooses winner
    """
    players = {'Maria': 0, 'Ben': 0}

    for num in nums:
        primes = sieve_of_eratosthenes(num)
        if len(primes) % 2 == 0:
            players['Ben'] += 1
        else:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None

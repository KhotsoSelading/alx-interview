#!/usr/bin/python3
"""
Topic: Prime Game
Author: Khotso Selading
Date: 10-03-2024
"""


def generate_primes(limit):
    """
    Finds prime number
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(limit + 1) if primes[i]]


def determine_winner(n):
    """
    Deteremines winner
    """
    primes = generate_primes(n)
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"


def isWinner(x, nums):
    """
    Gets winner
    """
    maria_wins = ben_wins = 0
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

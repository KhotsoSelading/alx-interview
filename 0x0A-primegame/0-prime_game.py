#!/usr/bin/python3
"""
Topic: Prime Game
Author: Khotso Selading
Date: 10-03-2024
"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a
    prime number from the set and removing that number and its
    multiples from the set.

    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.

    Args:
    - x (int): Number of rounds.
    - nums (list of int): An array of n for each round.

    Returns:
    - str or None: Name of the player that won the most rounds.
                   If the winner cannot be determined, returns None.
    """

    def sieve(n):
        """
        This is an algorithm to efficiently find all prime numbers up to n.
        """
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return primes

    def winner_of_round(n):
        """
        Function to determine the winner for a specific round based on the
        number of primes up to n obtained from the sieve.
        """
        primes = sieve(n)
        count = sum(primes[1:n+1])
        return "Maria" if count % 2 == 0 else "Ben"

    winners = [winner_of_round(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

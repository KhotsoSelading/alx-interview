#!/usr/bin/python3
"""
Topic: Making change
Author: Khotso Selading
Date: 26-02-2024
"""


def makeChange(coins, total):
    """
    Function that calculates the fewest number of coins
    needed to meet a given total.

    Args:
    - coins (list of int): The values of the coins in your possession.
    - total (int): The target total to be met.

    Returns:
    - int: The fewest number of coins needed to meet the total.
           If the total is 0 or less, return 0.
           If the total cannot be met by any number of coins you have,
           return -1.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

#!/usr/bin/python3

"""
Topic: Lockboxes
Author: Khotso Selading
Date: 08-01-2024
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened .

    param: boxes
    return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and 0 <= key < len(boxes):
                unlocked.append(key)

    return len(unlocked) == len(boxes)

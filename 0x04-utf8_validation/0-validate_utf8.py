#!/usr/bin/python3
"""
Topic: utf8-Validation
Author: Khotso Selading
Date: 29-01-2024
"""


def validUTF8(data) -> bool:
    """ A method that determines if a given data set represents a valid UTF-8
    encoding.

    param (data): a list of integers
    return: True if data is a valid UTF-8 encoding, else return False
    """
    byte_number = 0

    for byte in data:
        mask = 1 << 7

        if not byte_number:
            while byte & mask:
                byte_number += 1
                mask >>= 1
            if not byte_number:
                continue
            if byte_number == 1 or byte_number > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        byte_number -= 1

    return byte_number == 0

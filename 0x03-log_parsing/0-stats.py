#!/usr/bin/python3
"""
Topic: Log Parsing
Author: Khotso Selading
Date: 22-01-2024
"""

import sys

if __name__ == '__main__':

    filesize = 0
    count = 0
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("Total File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line_spliter in sys.stdin:
            count += 1
            data = line_spliter.split()
            try:
                status_code = data[-2]
                if status_code in codes:
                    stats[status_code] += 1
            except IndexError:
                pass
            try:
                filesize += int(data[-1])
            except (ValueError, IndexError):
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)

    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise

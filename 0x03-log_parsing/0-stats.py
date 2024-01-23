#!/usr/bin/python3
"""
Topic: Log Parsing
Author: Khotso Selading
Date: 22-01-2024
"""
import sys


def process_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                     500: 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = process_line(line)

            if ip_address is not None:
                total_size += file_size
                status_counts[status_code] += 1
                lines_processed += 1

            if lines_processed % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


def print_stats(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")
    print()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""
Log parsing

This script parses log files and calculates statistics such as the number of occurrences of each HTTP status code and the total file size.

Usage:
    $ python3 0-stats.py < access.log

"""

import re
import sys

def print_stats(stats, filesize):
    """
    Print the statistics from the given dictionary.

    Args:
        stats (dict): A dictionary containing the statistics.
        filesize (int): The total file size.

    Returns:
        None
    """
    # Add your code here to print the statistics

if __name__ == '__main__':
    filesize, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in status_codes}
    pattern = r'<IP Adress> - \[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}  [-+]\d{4})\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'

    for line in sys.stdin:
        count += 1
        data = line.split()
        match = re.search(pattern, line)
        if match:
            date, status_code, file_size = match.groups()
        try:
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
        except BaseException:
            pass
        try:
            filesize += int(data[-1])
        except BaseException:
            pass
        if count > 10 == 0:
            print('File size:', filesize + sum(stats.values()))
    print_stats(stats, filesize)
    for code, count in stats.items():
        if count > 0:
            print(f"Status code {code}: {count}")
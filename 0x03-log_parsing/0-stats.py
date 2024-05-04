#!/usr/bin/python3
"""
This script reads log lines from stdin, computes metrics,
and prints statistics every 10 lines or on keyboard interruption.
"""

import sys
import re

total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
        match = re.match(pattern, line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_size += file_size
            status_counts[status_code] += 1
            line_count += 1

        if line_count == 10:
            print(f"File size: {total_size}")
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print(f"{code}: {status_counts[code]}")
            line_count = 0

except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
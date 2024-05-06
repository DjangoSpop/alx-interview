#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

# Dictionary to store the count of each status code
import re
import sys

status_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

total_size = 0
line_count = 0

# Regular expression pattern to match the log line format
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.+?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$'

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            status_code = match.group(3)
            file_size = int(match.group(4))

            # Update the total file size and status code count
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

        # Print statistSics after every 10 lines or on keyboard interruption
        if line_count == 10:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print(f"{code}: {status_counts[code]}")
            line_count = 0

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

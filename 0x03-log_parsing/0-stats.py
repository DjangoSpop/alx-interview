#!/usr/bin/python3
"""Log parsing module"""
import sys
import signal
import re


# Initialize variables
total_file_size = 0
status_code_counts = {}

# Regular expression pattern
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(\d+/\w+/\d+:\d+:\d+:\d+) \+\d+\] ' \
          r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$'


def signal_handler(signal, frame):
    """
    Handle keyboard interruption (CTRL + C)
    and print metrics.
    """
    print_metrics()


def print_metrics():
    """
    Print the computed metrics:
    - Total file size
    - Number of lines by status code
    """
    print(f"File size: {total_file_size}")
    sorted_codes = sorted(status_code_counts.keys())
    for code in sorted_codes:
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read input from stdin
line_count = 0
for line in sys.stdin:
    line_count += 1

    # Parse the input line
    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
            
    # Print metrics after every 10 lines
    if line_count % 10 == 0:
        print_metrics()
# Print metrics at the end
print_metrics()
#!/usr/bin/python3
"""
This script reads from stdin, line by line, and computes metrics based on the log entries.
Each log must follow the format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If the format does not match, the line is skipped. Metrics are printed after every valid log entry and upon interruption (CTRL + C).
"""

import sys
import re

# Regex pattern to match the log format
pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

# Valid status codes as a set for quick lookup
valid_status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}

# Dictionary to count occurrences of status codes
status_code_counts = {}
# Total file size
total_file_size = 0
# Line count
line_count = 0

try:
    for line in sys.stdin:
        # Check if the line matches the required format
        match = pattern.match(line)
        if match:
            # Extract status code and file size from the line
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Check if the status code is one of the valid codes
            if status_code in valid_status_codes:
                # Update total file size
                total_file_size += file_size
                # Update count of the current status code
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1

                # Print the statistics after processing each valid line
                print('File size:', total_file_size)
                for code in sorted(status_code_counts):
                    print(f"{code}: {status_code_counts[code]}")
except KeyboardInterrupt:
    # Handle CTRL + C interruption: print the current statistics
    print('File size:', total_file_size)
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")
    sys.exit("Interrupted by user")

# After exiting the loop (end of input), also print the statistics if needed
if line_count > 0:
    print('File size:', total_file_size)
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")

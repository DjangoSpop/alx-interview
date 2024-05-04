#!/usr/bin/python3
"""
Log stats module
This script reads from stdin line by line and computes metrics such as total file size
and the number of occurrences of each status code for formatted log entries.
"""

import sys
import re
from collections import defaultdict

def validate_format(log):
    """
    Validates if a log entry matches the required format:
    IP Address - [date] "GET /projects/260 HTTP/1.1" status_code file_size
    Returns True if the log is valid, False otherwise.
    """
    pattern = r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'
    return bool(re.match(pattern, log))

def parse_log(log):
    """
    Parses a log entry into status code and file size, assuming the format is valid.
    Returns a tuple (status_code, file_size).
    """
    parts = log.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def print_stats(file_size, status_codes):
    """
    Prints the statistics for file size and status codes.
    """
    print('File size:', file_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """
    Continuously reads log entries from stdin, validates their format,
    and prints cumulative metrics every 10 lines or upon a keyboard interruption.
    """
    status_codes_count = defaultdict(int)
    total_size = 0
    log_count = 0

    try:
        for log in sys.stdin:
            if validate_format(log):
                status_code, file_size = parse_log(log)
                total_size += file_size
                status_codes_count[status_code] += 1
                log_count += 1

                if log_count % 10 == 0:
                    print_stats(total_size, status_codes_count)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes_count)
        sys.exit("Interrupted by user")

    # In case the stream ends without an interrupt
    if log_count % 10 != 0:
        print_stats(total_size, status_codes_count)

if __name__ == '__main__':
    main()

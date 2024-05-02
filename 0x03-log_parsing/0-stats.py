#!/usr/bin/python3

import sys
import re

def log_parser():
    """
    Parses log entries from stdin and calculates file size and status code counts.

    This function reads log entries from the standard input and performs the following tasks:
    - Calculates the total file size by summing the file sizes in the log entries.
    - Counts the occurrences of different HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).

    The log entries are expected to have the following format:
    <IP address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    The function prints the file size and the count of each status code every 10 log entries.

    Raises:
        None

    Returns:
        None
    """
    file_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(r'^[\d+\.]+\s-\s\[.+\]\s"GET\s\/projects\/260\sHTTP\/1\.1"\s(\d+)\s(\d+)$', line)
            if match:
                status_code = int(match.group(1))
                file_size += int(match.group(2))
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count % 10 == 0:
                print("File size: {}".format(file_size))
                for code in sorted(status_counts.keys()):
                    if status_counts[code] > 0:
                        print("{}: {}".format(code, status_counts[code]))

    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print("{}: {}".format(code, status_counts[code]))

log_parser()

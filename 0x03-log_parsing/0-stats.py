#!/usr/bin/python3
import sys
import re

def parse_line(line):
    """
    Parse a log line and extract the status code and file size.

    Args:
        line (str): The log line to parse.

    Returns:
        dict: A dictionary containing the status code and file size if the line is valid,
              otherwise None.
    """
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return {'status_code': status_code, 'file_size': file_size}
    return None

def print_stats(total_size, status_counts):
    """
    Print the total file size and the count of each status code.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing the count of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    """
    The main function that reads log lines from stdin, parses them, and prints statistics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed:
                status_code = parsed['status_code']
                file_size = parsed['file_size']
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
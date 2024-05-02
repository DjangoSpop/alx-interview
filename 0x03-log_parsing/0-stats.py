#!/usr/bin/python3
import sys
import datetime

def parse_log_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except ValueError:
        return None

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parsed = parse_log_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
            if line_count == 10:
                print_statistics(total_size, status_counts)
                line_count = 0
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

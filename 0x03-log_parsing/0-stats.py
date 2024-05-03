#!/usr/bin/python3
import sys

def parse_log_line(line):
    """
    Parses a log line and extracts the status code and file size.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple containing the status code and file size if the line is valid, otherwise None.
    """
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
    """
    Prints the total file size and the count of each status code.

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

    It reads log lines from stdin, parses each line using the `parse_log_line` function,
    updates the total file size and status code counts, and prints statistics every 10 lines.
    If the program is interrupted by a keyboard interrupt (Ctrl+C), it prints the final statistics.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_log_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print_statistics(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
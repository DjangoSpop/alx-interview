#!/usr/bin/python3
import sys
#createing a log parser with python
def print_stats(total_size, status_codes):
    """
    Prints the total file size and the count of each status code.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing the count of each status code.
    """
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """
    Parses a line of input and returns the IP address, status code, and file size.

    Args:
        line (str): A line of input in the format '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'.

    Returns:
        tuple: A tuple containing the IP address, status code, and file size, or None if the line is not in the expected format.
    """
    parts = line.split()
    if len(parts) < 7:
        return None
    ip, _, _, _, status_code, file_size = parts[:6]
    if not status_code.isdigit():
        return None
    return ip, int(status_code), int(file_size)

def main():
    """
    The main function that reads from stdin, computes the metrics, and prints the statistics.
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed = parse_line(line)
            if parsed is None:
                continue

            ip, status_code, file_size = parsed
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
    
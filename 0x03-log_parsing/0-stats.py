#!/usr/bin/python3
import sys


def parse_log_line(line):
    """
    Parse a log line and extract the IP address, status code, and file size.

    Args:
        line (str): The log line to parse.

    Returns:
        tuple: A tuple containing the IP address, status code, and file size.
    """
    try:
        parts = line.strip().split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except Exception as e:
        return None, None, None


def main():
    """
    Read log lines from standard input, parse them, and calculate statistics.

    The function reads log lines from standard input and parses each line to extract the IP address,
    status code, and file size. It then updates the total file size and counts the occurrences of
    each status code. After processing 10 lines, it prints the total file size and the count of each
    status code. The function handles keyboard interrupts and prints the statistics before exiting.
    """
    total_file_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_log_line(line)
            if ip_address is not None and status_code is not None and file_size is not None:
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print("Total file size:", total_file_size)
                for code in sorted(status_code_counts.keys()):
                    if status_code_counts[code] > 0:
                        print(f"{code}: {status_code_counts[code]}")
                line_count = 0

    except KeyboardInterrupt:
        print("Total file size:", total_file_size)
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code] > 0:
                print(f"{code}: {status_code_counts[code]}")
        sys.exit(0)


if __name__ == "__main__":
    main()

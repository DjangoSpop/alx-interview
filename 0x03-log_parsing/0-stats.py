import sys
import re
from collections import defaultdict

def validate_format(log):
    """
    Validates the format of a log entry.

    Args:
        log (str): The log entry to validate.

    Returns:
        bool: True if the log entry is in the correct format, False otherwise.
    """
    pattern = r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'
    return bool(re.match(pattern, log))

def parse_log(log):
    """
    Parses a log entry and extracts the status code and file size.

    Args:
        log (str): The log entry to parse.

    Returns:
        tuple: A tuple containing the status code (str) and file size (int).
    """
    parts = log.split()
    status_code = parts[-2]
    file_size = int(parts[-1])
    return status_code, file_size

def print_stats(file_size, status_codes):
    """
    Prints the file size and the count of each valid status code.

    Args:
        file_size (int): The total file size.
        status_codes (dict): A dictionary containing the count of each status code.

    Returns:
        None
    """
    valid_status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    print('File size:', file_size)
    for code in sorted(status_codes.keys()):
        if code in valid_status_codes:
            print(f"{code}: {status_codes[code]}")

status_codes_count = defaultdict(int)
total_size = 0
log_count = 0

try:
    for log in sys.stdin:
        if validate_format(log):
            status_code, file_size = parse_log(log)
            total_size += file_size
            if status_code in {"200", "301", "400", "401", "403", "404", "405", "500"}:
                status_codes_count[status_code] += 1
            log_count += 1

        if log_count % 10 == 0:
            print_stats(total_size, status_codes_count)

except KeyboardInterrupt:
    print_stats(total_size, status_codes_count)
    sys.exit("Interrupted by user")

if log_count % 10 != 0 or log_count == 0:
    print_stats(total_size, status_codes_count)

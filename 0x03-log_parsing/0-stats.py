import sys
#log parsing
def print_stats(total_size, status_codes):
    """
    Print the total file size and the count of each status code.

    Args:
        total_size (int): The total size of the file.
        status_codes (dict): A dictionary containing the count of each status code.
    """    
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """_summary_

    Args:
        line (_type_): _description_

    Returns:
        _type_: _description_
    """    
    parts = line.split()
    if len(parts) < 7:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None
    return ip_address, int(status_code), int(file_size)

def process_logs():
    """
    Process logs from standard input and calculate statistics.

    This function reads log lines from the standard input, parses each line,
    and calculates statistics such as total size and status code counts.
    It prints the statistics every 10 lines, and also handles keyboard interrupt
    to print the final statistics.

    Args:
        None

    Returns:
        None
    """

    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed_line = parse_line(line)
            if parsed_line is None:
                continue
 
            _, status_code, file_size = parsed_line
            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

process_logs()

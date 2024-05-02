import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

def print_metrics():
    """
    Print the computed metrics:
    - Total file size
    - Number of lines by status code
    """
    print(f"File size: {total_file_size}")
    sorted_codes = sorted(status_code_counts.keys())
    for code in sorted_codes:
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    """
    Handle keyboard interruption (CTRL + C)
    """
    print_metrics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
for i, line in enumerate(sys.stdin, start=1):
    try:
        parts = line.split(' ')
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
            total_file_size += file_size
    except (IndexError, ValueError):
        continue

    if i % 10 == 0:
        print_metrics()

# Print final metrics
print_metrics()
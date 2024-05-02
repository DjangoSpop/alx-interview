import sys

# Function to print statistics
def print_stats(total_size, status_counts):
    print(f"Total file size: {total_size}")

    # Sort the status codes in ascending order
    sorted_codes = sorted(status_counts.keys())

    # Print the count for each status code
    for code in sorted_codes:
        count = status_counts[code]
        if count > 0:
            print(f"{code}: {count}")

# Function to parse a line of input
def parse_line(line):
    parts = line.split()

    # Check if the line has at least 7 parts
    if len(parts) < 7:
        return None

    status_code = parts[5]
    file_size = parts[6]

    # Check if the status code is a valid integer
    if not status_code.isdigit():
        return None

    # Return the status code and file size as integers
    return int(status_code), int(file_size)

def main():
    total_size = 0
    status_counts = {}

    # Initialize a list of possible status codes
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    # Initialize the counts for each status code to 0
    for code in status_codes:
        status_counts[code] = 0

    line_count = 0

    try:
        # Read lines from stdin
        for line in sys.stdin:
            line_count += 1

            # Parse the line and extract the status code and file size
            parsed = parse_line(line)
            if parsed is None:
                continue

            status_code, file_size = parsed

            # Update the total file size and the count for the status code
            total_size += file_size
            status_counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print final statistics if the user interrupts the script
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
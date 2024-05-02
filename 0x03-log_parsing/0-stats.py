import sys

# Function to print statistics
def print_stats(total_size, counts):
    print(f"Total file size: {total_size}")

    # Print counts for each status code
    print_code(200, counts)
    print_code(301, counts)
    print_code(400, counts)
    print_code(401, counts)
    print_code(403, counts)
    print_code(404, counts)
    print_code(405, counts)
    print_code(500, counts)

# Helper function to print count for a specific status code
def print_code(code, counts):
    if code in counts:
        print(f"{code}: {counts[code]}")

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
    counts = {}

    # Initialize counts for each status code to 0
    counts[200] = 0
    counts[301] = 0
    counts[400] = 0
    counts[401] = 0
    counts[403] = 0
    counts[404] = 0
    counts[405] = 0
    counts[500] = 0

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
            counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        # Print final statistics if the user interrupts the script
        print_stats(total_size, counts)

if __name__ == "__main__":
    main()
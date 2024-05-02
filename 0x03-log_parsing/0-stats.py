import sys

# This function prints the statistics
def print_stats(total_size, status_counts):
    """
    Prints the total file size and the count of each status code.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary containing the count of each status code.
    """
    print(f"Total file size: {total_size}")  # Print the total file size

    # Print the count of each status code in ascending order
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        if count > 0:  # Only print if the status code appeared in the input
            print(f"{status_code}: {count}")

# This function parses a line of input and extracts the status code and file size
def parse_line(line):
    """
    Parses a line of input and returns the status code and file size.

    Args:
        line (str): A line of input in the format '<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>'.

    Returns:
        tuple: A tuple containing the status code and file size, or None if the line is not in the expected format.
    """
    # Split the line into parts
    parts = line.split()

    # Check if the line has at least 7 parts (IP, date, GET, status code, file size)
    if len(parts) < 7:
        return None

    # Extract the status code and file size from the parts
    status_code, file_size = parts[5], parts[6]

    # Check if the status code is a valid integer
    if not status_code.isdigit():
        return None

    # Return the status code and file size as integers
    return int(status_code), int(file_size)

def main():
    """
    The main function that reads from stdin, computes the metrics, and prints the statistics.
    """
    total_size = 0  # Initialize the total file size to 0
    status_counts = {  # Initialize a dictionary to store the count of each status code
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0  # Initialize a counter to keep track of the number of lines

    try:
        # Read lines from stdin
        for line in sys.stdin:
            line_count += 1  # Increment the line count

            # Parse the line and extract the status code and file size
            parsed = parse_line(line)
            if parsed is None:
                continue  # Skip this line if it's not in the expected format

            status_code, file_size = parsed

            # Update the total file size and the count of the status code
            total_size += file_size
            status_counts[status_code] += 1

            # Print the statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print the final statistics if the user interrupts the script with CTRL+C
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
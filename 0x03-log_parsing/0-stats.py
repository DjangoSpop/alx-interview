#!/usr/bin/python3
#createimport sys
import re
import signal
"""_summary_

    Raises:
        TimeoutError: _description_
"""
# Setting up the counters
total_size = 0
line_count = 0
status_codes_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405' : 0, '500' : 0}
 
# Regex to check the correct format of each line
line_format = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \[(.*?)\] "(GET|POST|DELETE) /project/.* HTTP/1\.[01]" (\d{3}) \d+$')

def handle_timeout(signum, frame):
    raise TimeoutError

# Set up signal for every 10 lines
signal.signal(signal.SIGALRM, handle_timeout)

import re

line_format = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "(.*?)" (\d{3})')

def parse_line(line):
    """Parses a log line and updates the status code count and total size.

    Args:
        line (str): The log line to parse.

    """
    global total_size, line_count
    match = line_format.match(line)
    if match:
        ip, date, method, status_code = match.groups()
        # Update status code count and total size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        # Simulating file size increment
        total_size += len(line)  # Example increment, adjust as needed
        line_count += 1

try:
    while True:
        try:
            # Set an alarm for 10 lines
            if line_count % 10 == 0:
                signal.alarm(1)  # Set the alarm for 1 second, adjust as needed
            line = input()
            parse_line(line)
        except TimeoutError:
            print("Processed 10 lines.")
            print(f"Total Size: {total_size}")
            print(f"Status Codes: {status_codes_count}")
            # Reset the alarm
            signal.alarm(0)
except KeyboardInterrupt:
    print("Program terminated by user.")
    print(f"Final Total Size: {total_size}")
    print(f"Final Status Codes: {status_codes_count}")

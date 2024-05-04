#!/usr/bin/python3
"""
This script reads log data from stdin and computes metrics such as total file size
and the number of occurrences of each status code. It expects each log entry to be in a specific format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
If an entry does not match this format, it is skipped. Metrics are printed after each log entry and upon program exit.
"""

import sys
import re
from collections import defaultdict

status_codes_count = defaultdict(int)
total_size = 0
log_count = 0
valid_status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
pattern = r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\] "GET /projects/260 HTTP/1\.1" \d{3} \d+$'

try:
    for log in sys.stdin:
        if re.match(pattern, log):
            parts = log.split()
            status_code = parts[-2]
            file_size = int(parts[-1])
            if status_code in valid_status_codes:
                total_size += file_size
                status_codes_count[status_code] += 1
                log_count += 1
                # Print current statistics
                print('File size:', total_size)
                for code in sorted(status_codes_count.keys()):
                    print(f"{code}: {status_codes_count[code]}")
except KeyboardInterrupt:
    # Print statistics if interrupted
    print('File size:', total_size)
    for code in sorted(status_codes_count.keys()):
        print(f"{code}: {status_codes_count[code]}")
    sys.exit("Interrupted by user")

if log_count == 0:
    print("No valid log entries processed.")
else:
    # Print final stats if any logs were processed
    print('File size:', total_size)
    for code in sorted(status_codes_count.keys()):
        print(f"{code}: {status_codes_count[code]}")

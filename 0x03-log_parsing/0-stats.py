#!/usr/bin/python3
"""
Log parsing
"""
import re
import sys
"""
we can create a fucnction
to make a log parsing script
"""
if __name__ == '__main__':

    filesize, count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}
    pattern = r'<IP Adress> - \[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}  [-+]\d{4})\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    
        """
        Print the statistics from the given dictionary.

        Args:
            stats (dict): A dictionary containing the statistics.

        Returns:
            None
        """
        
    try:
        for line in sys.stdin :
            count += 1
            data = line.split()
             match = re.search(pattern, line)
            if match:
                date, status_code, file_size = match.groups()    
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(status_code, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise

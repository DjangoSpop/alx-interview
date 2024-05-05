#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys
import re

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
date_pattern = r'\d{4}-\d{2}-\d{2}'
time_pattern = r'\d{2}:\d{2}:\d{2}'
request_pattern = r'\"[A-Z]{3,7} \/.*?\"'
status_pattern = r'\d{3}'
size_pattern = r'\d+'

for line in sys.stdin:
    match = re.match(f'({ip_pattern}) - \[({date_pattern}) ({time_pattern})\] {request_pattern} ({status_pattern}) ({size_pattern})', line)
    if match:
        code = match.group(5)
        size = int(match.group(6))
        if code in cache:
            cache[code] += 1
        total_size += size
        counter += 1

    if counter == 10:
        counter = 0
        print('Total file size:', total_size)
        for key, value in sorted(cache.items()):
            if value != 0:
                print(key + ':', value)
try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('Total file size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    print('Total file size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

except Exception as err:
    print('Error: {}'.format(err))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

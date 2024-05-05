#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys
import re
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0
pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$'
try:
    for line in sys.stdin:
        line_list = re.findall(pattern, line)
        if line_list:
            size = int(line_list[0][3])
            code = line_list[0][2]
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
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
        if line_list[7].isdigit():
            size = int(line_list[7])
        else:
            continue
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
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

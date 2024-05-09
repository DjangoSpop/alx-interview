#!/usr/bin/python3\
"""utf-8 validation module"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding"""
    byte_count = 0
    for byte in data:
        byte = byte & 255
        if byte_count:
            if byte >> 6 != 2:
                return False
            byte_count -= 1
        else:
            if byte >> 7 == 0:
                continue
            while (1 << abs(7 - byte_count)) & byte:
                byte_count += 1
            if byte_count == 1 or byte_count > 4:
                return False
            byte_count = max(byte_count - 1, 0)
    return byte_count == 0

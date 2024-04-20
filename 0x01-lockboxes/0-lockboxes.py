#!/usr/bin/python3
"""
Module that solves the problem of unlocking all boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists, where each inner list represents
                      the keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    unlocked = [0]  # Start with box 0 unlocked
    keys = boxes[0]  # Keys found in box 0

    for box_id in keys:
        if box_id < len(boxes) and box_id not in unlocked:
            unlocked.append(box_id)
            keys.extend(boxes[box_id])

    return len(unlocked) == len(boxes)

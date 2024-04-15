#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    if not boxes:
        return False
    if not boxes[0]:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)

#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened

    Args:
        boxes (arr[int]): Boxes contains the key to open other boxes

    Return:
        (bool): True otherwise false
    """
    unlocked = [0]
    for boxID, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != boxID:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False

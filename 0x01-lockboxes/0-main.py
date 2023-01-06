#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll
canUnlockAll2 = __import__('0-lockboxes').canUnlockAll2

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll2(boxes))
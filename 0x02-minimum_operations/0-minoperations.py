#!/usr/bin/python3
"""calculates the fewest number of operations needed to result
    in exactly n H characters in the file
"""


def minOperations(n: int) -> int:
    """Minimum operation"""
    if not isinstance(n, int) or n < 2:
        return 0

    prev = 1
    operations = cur = value = 2

    while n > value:
        reminder = n - value
        if reminder % cur == 0:
            operations += 2
            prev = cur
            value += cur
            cur = value
        elif reminder % prev == 0:
            operations += 1
            value += prev
            cur = value
    return operations

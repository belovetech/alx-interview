#!/usr/bin/python3
"""UTF-8 Validation
  Determines if a given data set represents a valid UTF-8 encoding.
"""


masks = [128, 64, 32, 16, 8]


def getType(num: int) -> int:
    """Get type
    """
    for i in range(len(masks)):
        if (masks[i] & num) == 0:
            return i
    return -1


def validUTF8(data: list[int]) -> bool:
    """Determines if a given data set represents
     a valid UTF-8 encoding or not
    """
    for i in range(len(data)):
        curr = data[i]
        type = getType(curr)

        if type == 0:
            continue
        elif type > 1 and i + type <= len(data):
            while type > 1:
                type -= 1
                i += 1
                if getType(data[i]) != 1:
                    return False
        else:
            return True
    return True

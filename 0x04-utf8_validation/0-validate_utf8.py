#!/usr/bin/python3
"""UTF-8 Validation
Determines if a given data set represents a valid UTF-8 encoding.
"""


def getType(num):
    """Check the type
    """
    masks = [128, 64, 32, 16, 8]
    for i in range(len(masks)):
        if (masks[i] & num) == 0:
            return i
    return -1


def validUTF8(data):
    """Determines if a given data set represents
     a valid UTF-8 encoding or not
    """
    for i in range(len(data)):
        curr = data[i]
        _type = getType(curr)

        if _type == 0:
            continue
        elif _type > 1 and i + _type <= len(data):
            while _type > 1:
                _type -= 1
                i += 1
                if getType(data[i]) != 1:
                    return False
        else:
            return True
    return True

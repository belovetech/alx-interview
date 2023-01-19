#!/usr/bin/python3
"""Log Parsing
Write a script that reads stdin line by line and computes metrics:
"""
import sys


total_file_size = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
obj = dict.fromkeys(status, 0)

def printLogStat():
    """Print log statistics"""
    print("File size: {}".format(total_file_size))
    for key, value in obj.items():
        if value > 0:
            print("{}: {}".format(key, value))

if __name__ == "__main__":
    count = 0
    try:
        for line in sys.stdin:
            try:
                line = line.split()
                total_file_size += int(line[-1])

                code = int(line[-2])
                if code in status:
                    obj[code] = obj.get(code, 0) + 1

            except Exception:
                pass
            count += 1

            if count % 10 == 0:
                printLogStat()
                
    except KeyboardInterrupt:
        printLogStat()
        raise
    else:
        printLogStat()

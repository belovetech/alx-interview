#!/usr/bin/python3
"""Log Parsing
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import signal


def handler(signum, frame):
    """Keyboard interruption handler"""
    print(f"File size: {total_file_size}")
    exit(0)


signal.signal(signal.SIGINT, handler)


count = 0
total_file_size = 0
status = [200, 301, 400, 401, 403, 404, 405, 500]
obj = dict.fromkeys(status, 0)

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break

    count += 1

    line = line.split()
    total_file_size += int(line[8])

    code = int(line[7])
    if code in status:
        obj[code] = obj.get(code, 0) + 1

    if count % 10 == 0:
        print(f"File size: {total_file_size}")

        for key, value in obj.items():
            if value > 0:
                print(f"{key}: {value}")

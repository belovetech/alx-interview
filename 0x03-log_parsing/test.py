import random

status = [200, 301, 400, 401, 403, 404, 405, 500]
code = random.choice(status)

obj = {}

for s in status:
    obj[s] = 1

for i in range(10):
    if code in status:
        code = random.choice(status)
        print(type(code))
        obj[code] = 1 + obj.get(code) if obj[code] else 0
    # print(code)

print(obj)
# print(obj.get(200))
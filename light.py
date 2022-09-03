from itertools import count
from unittest import result


def countlight():
    result = 0
    lights = [False] * 100
    for i in range(100):
        for id in range(len(lights)):
            if (id+1)%(i+1) == 0:
                if lights[id]:
                    lights[id] = False
                else:
                    lights[id] = True
    for id in range(len(lights)):
        if lights[id]:
            result += 1
    return result

print(countlight())
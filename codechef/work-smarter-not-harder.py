import math

t = int(input())

for _ in range(t):
    l, v, v1 = map(int, input().split())

    tortoise = math.ceil(l / v)
    here = math.ceil(l / v1)

    if tortoise <= here:
        print(-1)
    else:
        print(tortoise - here - 1)
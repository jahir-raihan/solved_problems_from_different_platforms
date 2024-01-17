import math

t = int(input())

for _ in range(t):
    h, x, y1, y2, k = map(int, input().split())

    x = math.ceil(h / x)
    y = math.ceil(h / y1)
    if y > k:
        tmp = math.ceil((h - (k * y1)) / y2)
        y = k + tmp

    print(min(x, y))
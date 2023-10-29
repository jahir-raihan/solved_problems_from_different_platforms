import math
t = int(input())


def range_sum(l, r):
    if l > r:
        return 0
    return (l + r) * (r - l + 1) // 2


for _ in range(t):
    n, x, y = map(int, input().split())
    l = x * y // math.gcd(x, y)
    plus = n // x - n // l
    minus = n // y - n // l
    print(range_sum(n - plus + 1, n) - range_sum(1, minus))


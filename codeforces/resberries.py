t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    res = k
    even = 0

    for i in a:
        if i % 2 == 0:
            even += 1
        if i % k == 0:
            res = 0
        res = min(res, k - i % k)

    if k == 4:
        res = 0 if even > 1 else min(res, 1) if even > 0 else min(res, 2)
    print(res)
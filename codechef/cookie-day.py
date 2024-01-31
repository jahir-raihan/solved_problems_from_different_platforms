t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = [int(i) for i in input().split()]

    res = 999999999999999
    for i in a:
        if i >= k:
            res = min(i % k, res)

    print(res if res != 999999999999999 else -1)
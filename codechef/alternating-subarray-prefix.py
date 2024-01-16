t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = [1] * n

    for i in range(n - 2, -1, -1):
        if a[i] > 0 > a[i + 1] or a[i] < 0 < a[i + 1]:
            res[i] += res[i + 1]

    print(*res)
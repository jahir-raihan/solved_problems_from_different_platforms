t = int(input())
for _ in range(t):
    n = int(input())
    a = [(int(x), i) for i, x in enumerate(input().split())]
    a.sort()
    res = [0] * n
    for i in range(n):
        res[a[i][1]] = n - i
    print(*res)

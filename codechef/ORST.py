t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = [int(i) for i in input().split()]
    b = max([int(i) for i in input().split()])

    res = a[:n - b] + sorted(a[n - b:])
    print(*res)

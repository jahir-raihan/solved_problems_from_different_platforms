t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    a.sort()
    b.sort(reverse=1)

    s = set()

    for i in range(n):
        s.add(a[i] + b[i])

    if len(s) != 1:
        print(-1)
    else:
        print(*a)
        print(*b)
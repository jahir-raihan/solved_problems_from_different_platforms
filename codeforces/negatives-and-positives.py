t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    neg = 0
    for i in a:
        if i < 1:
            neg += 1
    a.sort()
    res = 0
    for i in range(n):
        res += abs(a[i])
    smallest = 99999999999
    if neg % 2 == 1:
        for i in a:
            smallest = min(abs(i), smallest)
        res -= smallest * 2

    print(res)

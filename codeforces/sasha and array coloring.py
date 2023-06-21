t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    res = 0
    i, j = 0, n - 1
    while j > i:
        res += a[j] - a[i]
        i += 1
        j -= 1
    print(res)

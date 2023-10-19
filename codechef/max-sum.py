

for _ in range(int(1)):
    n = 10
    arr = [5, 3, 6, 5, 6, 8, 4, 3, 2, 8]

    l = [0] * n
    r = [0] * n

    l[0] = arr[0]
    r[-1] = arr[-1]
    for i in range(1, n):
        l[i] = max(l[i - 1], arr[i])
        r[n - i - 1] = max(r[n - i], arr[n - i - 1])

    s = 0
    for i in range(n):
        s += min(l[i], r[i])
    print(s)
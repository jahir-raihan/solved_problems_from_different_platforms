t = 1
for _ in range(t):
    n, k = 4,2
    for i in range(n, 0, -1):
        a = n // i
        if a >= k:
            break
    ans = []
    v = i
    while k:
        ans += [v]
        k -= 1
        v += i
    print(*ans)
